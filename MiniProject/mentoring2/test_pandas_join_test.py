import numpy as np
import pandas as pd
import json
import hashlib
import time
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

    #testset_file1 = 'merge_to_csv100_encrypt.csv'
    #testset_file2 = 'merge_to_csv100_encrypt1.csv'
    testset_file1 = 'key_index_to_csv.csv'
    testset_file2 = 'key_index_to_csv1.csv'
 

    start = time.time()
    df1 = pd.read_csv(testset_file1)
    duration = time.time() - start
    print("csv load 1 = ", duration)

    start = time.time()
    df2 = pd.read_csv(testset_file2)
    duration = time.time() - start
    print("csv load 2 = ", duration)

    # start = time.time()
    # df_to_merge = pd.concat([df1, df2], axis=1)
    # duration = time.time() - start
    # print("csv merge = ", duration)
    #
    # print(df_to_merge.head())

    #df1_ = df1.set_index('IDX')
    #df2_ = df2.set_index('IDX')

    start = time.time()
    print("merge to start..")
    df_to_merge = pd.merge(df1, df2, how='outer', on='IDX').progress_apply(lambda x: x)
    duration = time.time() - start
    print("csv merge end time = ", duration)

    start = time.time()
    print("merge file to csv....")
    #np.savetxt("test_set_merge_outer2.csv", df_to_merge, delimiter=",", fmt="%s", header=','.join(df_to_merge.columns), comments='')
    df_to_merge.to_csv("huge_data_merge_outer_100.csv", sep=",", index=False)
    duration = time.time() - start
    print("save csv = ", duration)

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

def column_sum(df):
    sum_df = df['Unit Price'].sum()

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
