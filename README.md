# README
## 序言
这个项目的根本目的是为了督促我进行学习吧，也因为代码文件写的乱七八糟四分五裂。

于是就想着能将代码统一到一个项目中，这样呢也能避免重复配置环境以及重复编写我们的基本工具类。还有好处呢就是能够一定程度上进行封装。

同样的缺点也就暴露了，其一就是目录结构可能比较深，不易回顾。其二呢，代码封装可能比较低级。

就说这些吧先，后续也会将每段时间的一个历程、思路想法以及“打快板” ？写到这里，也算是自己的一种回顾。

## 目录结构
根据目前的形式来看，
```bash
PATH\LOKI
│  .gitignore
│  LICENSE
│  README.md
│  
├─.idea
│  │  .gitignore
│  │  deployment.xml
│  │  loki.iml
│  │  misc.xml
│  │  modules.xml
│  │  vcs.xml
│  │  webServers.xml
│  │  workspace.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│
├─data
│      .gitkeep
│      000016_6_8_m1.csv
│      000016_6_8_m1.xlsx
│      000016_6_8_m1_kit.csv
│
├─docs
│      .gitkeep
│      LSTM Neural Network for Time Series Prediction.md
│      创建数据集方案.md
│
├─src
│  ├─CHAOS
│  │  │  try_xkcd.ipynb
│  │  │  try_xkcd.py
│  │  │  股价涨跌概率预测.ipynb
│  │  │
│  │  ├─基于LSTM的时序模型
│  │  │      0_搭建LSTM.ipynb
│  │  │      1_尝试.ipynb
│  │  │
│  │  └─神经网络底层分析与案例
│  │          0_实践_单个神经元.ipynb
│  │          1_复盘_单个神经元的实现.ipynb
│  │          2_废弃_性别预测网络.ipynb
│  │          3_复现-性别预测神经网络.ipynb
│  │
│  ├─Classical Algorithms
│  │      五分点预测.ipynb
│  │      密度分布解析.ipynb
│  │      快速傅里叶变换.ipynb
│  │
│  ├─Decision Tree Forecast
│  │      test.ipynb
│  │      利用决策树.ipynb
│  │
│  ├─Miscellaneous
│  │  └─zhli_demo
│  │      ├─v1.0
│  │      │      lstmnetwork.py
│  │      │      mydataloader.py
│  │      │      test.ipynb
│  │      │      test.py
│  │      │      train_lstmnetwork.py
│  │      │
│  │      ├─v2.0
│  │      │  │  ls.png
│  │      │  │  lstmnetwork.py
│  │      │  │  mydataloader.py
│  │      │  │  test.ipynb
│  │      │  │  test.py
│  │      │  │  train_lstmnetwork.py
│  │      │  │
│  │      │  └─__pycache__
│  │      └─__pycache__
│  ├─Qbot
│  ├─Random Forest
│  ├─Strategy Library
│  │  └─Stocks
│  │      └─布林线均值回归
│  │              main.py
│  │              README.md
│  │
│  └─SVM
│          简单的尝试.ipynb
│
└─utils
        .gitkeep

```

其余的顾名思义。

首次编辑于： 2023-10-13 10:03 AM ShenZhen

最后编辑于： 2023-11-14 09:49 AM ShenZhen 
