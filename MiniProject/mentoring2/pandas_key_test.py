import numpy as np
import pandas as pd
import json
import hashlib
import time
import datetime
from tqdm import tqdm

tqdm.pandas()

#decorator pattern
def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.perf_counter()-t))
        return res
    return wrapper

def main():

    total_start = time.time()

    testset_file = 'user_data_small_ko.csv'
        
    start = time.time()
    print('start')
    df = pd.read_csv(testset_file)
    print('end')
    duration = time.time() - start
    times = str(datetime.timedelta(seconds=duration)).split(".")
    times = times[0]
    print('csv to read time = ', times)

    print(df.head())

    start = time.time()
    print('start')
    column_encrypt(df, 'IDX')
    print('end')
    duration = time.time() - start
    times = str(datetime.timedelta(seconds=duration)).split(".")
    times = times[0]
    print('data to deid time = ', times)

    print(df.head())

    start = time.time()
    df_result = df
    #df_result = df[['IDX']]
    df_result.rename_axis('INDEX_COLUMN', inplace=True)
    df_result.to_csv("key_index_to_csv.csv", sep=",", index=True)
    duration = time.time() - start
    times = str(datetime.timedelta(seconds=duration)).split(".")
    times = times[0]
    print('write to csv time = ', times)

    duration = time.time() - total_start
    times = str(datetime.timedelta(seconds=duration)).split(".")
    times = times[0]
    print("total time = ", times)

def column_replace(df, column_name):
    print("replace data")
    df[column_name] = df[column_name].progress_apply(lambda x: str(x)[:3]+"**")

    print(df.head(20))
    print(df.info())

def column_replace(df, column_name):
    print("replace data")
    df[column_name] = df[column_name].progress_apply(lambda x: str(x)[:2]+"**")

    print(df.head(20))
    print(df.info())


def column_mean(df, column_name):
    mean_value = df[column_name].mean()
    print("mean value = ", mean_value)

    df[column_name] = df[column_name].progress_apply(lambda x: mean_value)

    print(df.head(20))
    print(df.info())

def column_sum(df, column_name):
    sum_df = df[column_name].sum()

    df[column_name] = df[column_name].progress_apply(lambda x: sum_df)

    print(df.head(20))
    print(df.info())

def sha256Text(salt_value, text):
    return hashlib.sha256(salt_value.encode()+text.encode()).hexdigest()

def column_encrypt(df, column_name):
    print("column_encrypt")
    df[column_name] = df[column_name].progress_apply(lambda x: str(x).replace(str(x), sha256Text('password', str(x))))

    print(df.head(20))
    print(df.info())


if __name__ == "__main__":
    main()
