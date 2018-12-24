# 贝叶斯分类器
## 贝叶斯决策论(Bayesian decision theory)
    贝叶斯决策论是概率框架下实施决策的基本方法.
## 极大似然估计(Maximum Likelihood Estimation, 简称MLE)
    估计类条件概率的一种常用策略是先假定其具有某种确定的概率分布形式,<br/>
    再基于训练样本对概率分布的的参数进行估计<br/>
    改路模型的训练过程就是参数估计(parameter estimation)过程<br/>
    对于参数估计, 统计学界的两个学派分别提供了不同的解决方案: <br/>
        * 频率主义学派(Frequentist)认为参数虽然未知, 但却是客观存在的固定值, 因此可通过<br/>
        优化似然函数等准则来确定参数值;<br/>
        * 贝叶斯学派(Bayesian)认为参数是未观察到的随机变量, 其本身也可有分布, 因此可假定<br/>
        参数服从一个先验分布, 然后基于观测到的数据来计算参数的后验分布<br/>
## 朴素贝叶斯分类器(Naive Bayes Classifier)
    朴素贝叶斯分类器采用了"属性条件独立性假设"<br/>
    (attribute conditional independence assumption):<br/>
        对于已知类别, 假设所有属性相互独立. 换言之, 假设每个属性独立地对分类结果发生影响
## 半朴素贝叶斯分类器(semi-naive Bayes classifiers)
    "独依赖估计"(One-Dependent Estimator, ODE)是半朴素贝叶斯分类器最常用的一种策略.
## 贝叶斯网(Bayes network)
    亦称"信念网"(belief network)