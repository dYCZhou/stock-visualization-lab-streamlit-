import akshare as ak
import pandas as pd

def get_stock_data(symbol, start_date, end_date):
    try:
        df = ak.stock_zh_a_hist(
            symbol=symbol,
            period="daily",
            start_date=start_date,
            end_date=end_date,
            adjust="qfq"
        )

        if df is None or df.empty:
            return None

        # 统一列名为英文，方便画图
        df.rename(columns={
            "日期": "date",
            "开盘": "open",
            "收盘": "close",
            "最高": "high",
            "最低": "low",
            "成交量": "volume",
            "成交额": "amount"
        }, inplace=True)

        # 转换日期格式
        df["date"] = pd.to_datetime(df["date"])
        df.sort_values("date", inplace=True)
        df[["open", "high", "low", "close"]] = df[["open", "high", "low", "close"]].astype(float)

        print(df.head())

        return df

    except Exception as e:
        print(f"获取或处理数据时出错：{e}")
        return None
