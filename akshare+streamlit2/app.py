import streamlit as st
import plotly.graph_objects as go
from data import get_stock_data
import pandas as pd

# -------------------------
# Streamlit 页面布局
# -------------------------
st.set_page_config(page_title="A股历史日线看板", layout="wide")

st.sidebar.header("股票数据可视化")

# 侧边栏用户输入
symbol = st.sidebar.text_input("股票代码 (如 000001 表示平安银行)", "688327")
start_date = st.sidebar.text_input("开始日期 (YYYYMMDD)", "20250501")
end_date = st.sidebar.text_input("结束日期 (YYYYMMDD)", "20250817")

# -------------------------
# 获取数据按钮
# -------------------------
if st.sidebar.button("获取数据"):
    # 调用 data.py 中的函数获取股票历史日线
    df = get_stock_data(symbol, start_date, end_date)

    # 存入 session_state，保证页面刷新也能保留数据
    st.session_state["df"] = df

# -------------------------
# 从 session_state 读取数据
# -------------------------
df = st.session_state.get("df", None)

# 数据未获取时提示用户
if df is None or df.empty:
    st.info("请在左侧输入股票代码和日期，并点击获取数据")
else:
    # -------------------------
    # 图表类型选择
    # -------------------------
    chart_type = st.radio(
        "选择图表类型",
        ["K线图+成交量", "折线图"],
        key="chart_type"
    )



    if chart_type == "K线图+成交量":
        # -------------------------
        # 主图：K线图
        # -------------------------
        fig = go.Figure()

        # 绘制 K 线
        fig.add_trace(go.Candlestick(
            x=df["date"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            increasing_line_color="red",   # 上涨蜡烛红色
            decreasing_line_color="green", # 下跌蜡烛绿色
            name="K线"
        ))

        # -------------------------
        # 副图：成交量柱状图
        # -------------------------
        fig.add_trace(go.Bar(
            x=df["date"],
            y=df["volume"],
            name="成交量",
            marker_color="blue",
            yaxis="y2"  # 指定第二个 y 轴
        ))

        # -------------------------
        # 布局设置
        # -------------------------
        fig.update_layout(
            title=f"{symbol} 日线",
            xaxis_title="日期",
            yaxis_title="价格",
            yaxis2=dict(
                title="成交量",
                overlaying="y",   # 与主 y 轴叠加
                side="right",     # 显示在右侧
                showgrid=False
            ),
            xaxis_rangeslider_visible=False,  # 隐藏默认范围滑块
            template="plotly_white",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )



        # -------------------------
        # 渲染图表
        # -------------------------
        st.plotly_chart(fig, use_container_width=True)

        # 可选：显示前 5 行数据以供调试
        st.write("前5行数据预览：")
        st.write(df.head())

    elif chart_type == "折线图":
        # 简单折线图，显示收盘价
        st.line_chart(df.set_index("date")["close"])