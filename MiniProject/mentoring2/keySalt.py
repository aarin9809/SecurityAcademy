import pandas as pd
import pyarrow
import hashlib

'''
file key+salt 2개 파일 merge, 2개 file chunk 방식 merge
'''

file1 = './key_index_to_csv.csv'
file2 = './key_index_to_csv1.csv'

def hash_key_with_salt(key, salt):
    return hashlib.sha256((key + salt).encode()).hexdigest()

def merge_files_with_encryption(file1, file2, key_column, salt):
    # 파일을 불러옴
    df1 = pd.read_csv(file1, encoding='iso-8859-1')
    df2 = pd.read_csv(file2, encoding='iso-8859-1')
    
    # 키 컬럼을 암호화
    df1['encrypted_key'] = df1[key_column].apply(lambda x: hash_key_with_salt(x, salt))
    df2['encrypted_key'] = df2[key_column].apply(lambda x: hash_key_with_salt(x, salt))

    # 암호화된 키를 기반으로 파일 병합
    merged_df = pd.merge(df1, df2, on='encrypted_key')

    # 원래 키 컬럼 제거(선택사항)
    merged_df = merged_df.drop(columns=['encrypted_key', key_column + '_x', key_column + '_y'])

    return merged_df


merged_df = merge_files_with_encryption(file1, file2, key_column='name', salt='s3cr3t')
print(merged_df)