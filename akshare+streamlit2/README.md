# 📈 股票数据可视化看板 v2

本项目是股票可视化工具的 **第二代版本**，基于 **Streamlit** + **Plotly** + **AkShare** 构建。
相比第一代，本版本新增了 **K线图 + 成交量联动展示**，更贴近真实交易软件的视觉效果。

---

## 🚀 功能特性

* **输入股票代码 & 时间区间** → 获取 A 股历史日线数据
* **图表选择**：

  * 折线图：仅展示收盘价走势
  * K线图 + 成交量：主图为蜡烛图，副图为成交量柱状图（双 Y 轴）
* 数据来源：**AkShare**（免费开源金融数据接口）
* 前端基于 **Streamlit**，交互丝滑，浏览器即可运行
* 防御性编程：无数据时会提示用户，避免报错

---

## 📂 项目结构

```
├── app.py        # 主入口，Streamlit 界面 + 图表渲染逻辑
├── data.py       # 数据获取模块，封装 AkShare 调用与清洗
```

---

## ⚙️ 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/stock-visualization-v2.git
cd stock-visualization-v2
```

### 2. 安装依赖

建议使用虚拟环境：

```bash
pip install -r requirements.txt
```

requirements.txt 内容大致如下：

```
streamlit
plotly
akshare
pandas
```

### 3. 启动项目

```bash
streamlit run app.py
```

浏览器会自动打开 `http://localhost:8501`，即可使用新版股票看板。

---

## 📊 使用示例

* 输入股票代码：`000001` （平安银行）
* 输入日期范围：`20250501` 到 `20250817`
* 点击“获取数据” → 切换查看 **折线图** 或 **K线图 + 成交量**

K线图示例效果：

* 红色蜡烛：上涨
* 绿色蜡烛：下跌
* 蓝色柱状图：成交量（右侧 Y 轴）

---

## 🛠️ 技术栈

* **[Streamlit](https://streamlit.io/)**：轻量级 Web 应用框架
* **[Plotly](https://plotly.com/)**：交互式图表渲染
* **[AkShare](https://akshare.akfamily.xyz/)**：金融数据接口（股票、基金、期货等）
* **Pandas**：数据清洗与格式化

---

## 📌 TODO（未来计划）

* [ ] 添加更多技术指标（MACD、均线、布林带等）
* [ ] 支持多股票对比分析
* [ ] 优化图表样式，增加交互（缩放、拖拽、hover 提示）
* [ ] 支持一键部署到云端（Streamlit Cloud / Vercel）
