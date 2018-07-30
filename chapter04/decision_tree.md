# 决策树
## 划分选择
- 信息增益(Information gain)<br/>
    信息熵(Information entropy)是度量样本集合纯度最常用的一种指标
- 增益率(gain ratio)<br/>
- 基尼指数(Gini  Index)
## 剪枝处理
    剪枝(pruning)是决策树学习书法对付"过拟合"的主要手段
    决策树剪枝的基本策略有"预剪枝"(pre-pruning)和"后剪枝"(post-pruning)
        预剪枝是指在决策树生成过程中,对每个节点在划分前进行估计,若当前节点的划分
    不能带来决策树泛化性能提升,则停止划分并将当前节点标记为叶节点
        后剪枝则是先从训练集生成一颗完整的决策树,然后自底向下地对非叶节点进行
    考察,若将该节点对应的子树替换为叶节点能带来决策树泛化性能提升,则将该子树
    替换为叶节点
## 连续与缺失值
- 连续值处理
- 缺失值处理
## 多变量决策树(multivariate decision tree)