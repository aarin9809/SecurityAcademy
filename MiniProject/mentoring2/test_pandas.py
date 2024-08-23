# -*- coding: utf-8 -*-

import pandas as pd
import json
import hashlib
import time

def main():

    testset_file = 'test.csv'
    #pandas csv read
    df = pd.read_csv(testset_file, encoding="cp949")
    #dataframe 정보        
    df.info()
          
    column_replace(df, '이름')
    column_mean(df, '신장')
    column_sum(df, '월소득')
    column_encrypt(df, '직업종류')
   
       

def column_replace(df, column_name):
    print("replace data")
    df[column_name] = df[column_name].apply(lambda x: str(x)[:2]+"**")

    print(df.head(20))
    


def column_mean(df, column_name):
    mean_value = df[column_name].mean()
    print("mean value = ", mean_value)

    df[column_name] = df[column_name].apply(lambda x: mean_value)

    print(df.head(20))
    

def column_sum(df, column_name):
    sum_df = df[column_name].sum()

    df[column_name] = df[column_name].apply(lambda x: sum_df)

    print(df.head(20))
    

def sha256Text(salt_value, text):
    return hashlib.sha256(salt_value.encode()+text.encode()).hexdigest()

def column_encrypt(df, column_name):
    print("column_encrypt")
    df[column_name] = df[column_name].apply(lambda x: str(x).replace(str(x), sha256Text('password', str(x))))

    print(df.head(20))
    


if __name__ == "__main__":
    main()
