# import pandas as pd
# import matplotlib.pyplot as plt

# # 예제 데이터 생성
# data = pd.DataFrame({
#     'values': [10, 20, 20, 30, 30, 30, 40, 50, 60, 70]
# })

# # 히스토그램 그리기
# data['values'].hist(bins=5, edgecolor='black')
# plt.title('Histogram of Values')
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.show()


# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # 예제 데이터 생성
# data = pd.DataFrame({
#     'values': [10, 20, 20, 30, 30, 30, 40, 50, 60, 70]
# })

# # describe()로 요약 통계 출력
# print(data.describe())

# # 상자 그림(Boxplot) 시각화
# sns.boxplot(x=data['values'])
# plt.title('Boxplot of Values')
# plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# 예제 데이터 생성
np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)
data = pd.DataFrame({'x': x, 'y': y})

# 회귀분석 수행
model = np.polyfit(data['x'], data['y'], 1)
data['y_pred'] = np.polyval(model, data['x'])

# 잔차 계산
data['residuals'] = data['y'] - data['y_pred']

# 잔차의 히스토그램과 정규분포 곡선
sns.histplot(data['residuals'], kde=True, stat="density", linewidth=0)
plt.title('Residuals Histogram with Normal Distribution')
plt.xlabel('Residuals')

# 정규분포 곡선 추가
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, data['residuals'].mean(), data['residuals'].std())
plt.plot(x, p, 'k', linewidth=2)
plt.show()

# 잔차의 Q-Q 플롯
sns.qqplot(data['residuals'], line ='45')
plt.title('Q-Q Plot of Residuals')
plt.show()
