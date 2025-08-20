
# 📈 股票数据可视化看板

本项目是一个基于 **Streamlit** + **Plotly** + **AkShare** 的交互式股票数据可视化工具。
用户可以通过输入 **股票代码**、**时间区间**，快速获取 A 股的历史日线数据，并以 **折线图** 或 **K线图** 的方式进行展示。

---

## 🚀 功能特性

* 侧边栏输入股票代码、起止时间，点击按钮即可获取数据
* 支持展示 **收盘价折线图** 与 **K线图**
* 数据来源：**AkShare**（免费开源金融数据接口）
* 数据表格与图表同步展示，方便分析与调试
* 防御性编程：对数据获取失败或为空的情况有提示

---

## 📂 项目结构

```
├── app.py        # 主入口，Streamlit 前端交互与图表渲染
├── data.py       # 数据获取模块，封装了 AkShare 调用与清洗逻辑
```

---

## ⚙️ 安装与运行

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/stock-visualization.git
cd stock-visualization
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

浏览器会自动打开 `http://localhost:8501`，即可使用股票看板。

---

## 📊 使用示例

* 输入股票代码：`000001` （平安银行）
* 输入日期范围：如`20250101`  `20250817`
* 点击“获取数据” → 即可切换折线图 / K线图查看走势

---

## 🛠️ 技术栈

* **[Streamlit](https://streamlit.io/)**：快速搭建数据应用的 Python 框架
* **[Plotly](https://plotly.com/)**：高质量交互式可视化库
* **[AkShare](https://akshare.akfamily.xyz/)**：开源金融数据接口，支持股票、期货、基金等多种数据源
* **Pandas**：数据处理与清洗

