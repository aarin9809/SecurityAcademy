import pandas as pd
import pyarrow.csv as pc
import pyarrow as pa
import time

file = './5mSalesRecords.csv'

# start_time = time.time()    # 현재 시간을 초 단위로 반환하고 이를 출력한다.
# df_pandas = pd.read_csv(file)
# pandas_time = time.time() - start_time  # pandas 시간

# print(f"Pandas의 file loading 시간 : {pandas_time:.6f}초")

# table = pc.read_csv(file)  # pyarrow로 csv 읽기
# pyarrow_time = time.time() - start_time
# print(f"pyarrow의 file loading 시간 : {pyarrow_time:.6f}초")

import pyarrow.csv as pv
import pyarrow as pa
import pandas as pd
import time

# CSV 파일 경로
file_path = './5mSalesRecords.csv'

# Pandas만 사용한 경우의 시간 측정
start_time = time.time()
df_pandas = pd.read_csv(file_path)
pandas_time = time.time() - start_time
print(f"Pandas load time: {pandas_time:.6f} seconds")

# PyArrow를 사용한 경우의 시간 측정
start_time = time.time()
table = pv.read_csv(file_path)  # pyarrow로 csv 읽기
arrow_time = time.time() - start_time
print(f"PyArrow load time: {arrow_time:.6f} seconds")

# # PyArrow로 불러온 데이터를 Pandas DataFrame으로 변환
# start_time = time.time()
# df_arrow_pandas = table.to_pandas()
# arrow_to_pandas_time = time.time() - start_time
# print(f"PyArrow to Pandas conversion time: {arrow_to_pandas_time:.4f} seconds")

# # 전체 PyArrow + Pandas 시간
# total_arrow_time = arrow_time + arrow_to_pandas_time
# print(f"Total PyArrow + Pandas time: {total_arrow_time:.4f} seconds")

# # 결과 비교
# if pandas_time < total_arrow_time:
#     print(f"Pandas is faster by {total_arrow_time - pandas_time:.4f} seconds")
# else:
#     print(f"PyArrow is faster by {pandas_time - total_arrow_time:.4f} seconds")
