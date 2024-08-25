import pandas as pd
import pyarrow.csv as pc
import pyarrow.parquet as pq
import time

file = '5mSalesRecords.csv'

start_time = time.time()    # 현재 시간을 초 단위로 반환하고 이를 출력한다.
df_pandas = pd.read_csv(file)
pandas_time = time.time() - start_time  # pandas 시간

print(f"Pandas의 file loading 시간 : {pandas_time:.6f}초")

df_pyarrow = pc.read_csv(file)              #pyarrow로 파일 읽어오기
pyarrow_time = time.time() - start_time
print(f"pyarrow의 file loading 시간 : {pyarrow_time:.6f}초")

