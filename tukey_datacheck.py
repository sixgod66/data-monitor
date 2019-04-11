import numpy as np
import pandas as pd

## 基于tukey's method 的异常点排查
df = pd.DataFrame([
    [391398.5],
[398306.5],
[227108.4],
[184786.8],
[311340.4],
[169532.8],
[176233.4],
[362207.2],
[4983931.4],
[492169.8],
[355360],
[404346.5],
[240277.1],
[454136.3]
])
print(df[0])
## 第一四分位数
Q1 = np.percentile(df[0], 25)
## 第三四分位数
Q3 = np.percentile(df[0], 75)
## 四分位距
IQR = Q3-Q1
## 疑似异常值范围（1.5-3是温和异常值   3以上是极端异常值）
outlier_step = 1.5 * IQR
outlier_list_col = df[(df[0] < Q1 - outlier_step) | (df[0] > Q3 + outlier_step)].index

print('异常数据line number：')
for item in outlier_list_col:
    print(item)
