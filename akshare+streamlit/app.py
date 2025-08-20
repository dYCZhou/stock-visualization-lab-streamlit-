import streamlit as st
import plotly.graph_objects as go
from data import get_stock_data

st.sidebar.header("股票数据可视化")

# 侧边栏输入
symbol = st.sidebar.text_input("股票代码 (如 000001 表示平安银行)", "688327")
start_date = st.sidebar.text_input("开始日期 (YYYYMMDD)", "20250101")
end_date = st.sidebar.text_input("结束日期 (YYYYMMDD)", "20250817")

# 获取数据按钮
if st.sidebar.button("获取数据"):
    df = get_stock_data(symbol, start_date, end_date)
    st.session_state["df"] = df  # 保存到 session_state

# 从 session_state 读取数据
df = st.session_state.get("df", None)

if df is None or df.empty:
    st.info("请在左侧输入参数并点击获取数据")
else:
    # 图表选择
    chart_type = st.radio("选择图表类型", ["折线图", "K线图"], key="chart_type")

    if chart_type == "折线图":
        st.line_chart(df.set_index("date")["close"])

    elif chart_type == "K线图":

        fig = go.Figure(data=[go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            increasing_line_color="red",
            decreasing_line_color="green"
        )])
        fig.update_layout(
            title=symbol,
            xaxis_title="日期",
            yaxis_title="价格",
            xaxis_rangeslider_visible=False,
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
        st.write(df)  # 调试用
