import pandas as pd
import hashlib

# create synthetic data
data = {
    'name': ['John Doe', 'Jane Doe', 'Alice Smith', 'Bob Brown'],
    'email': ['john.doe@example.com', 'jane.doe@example.com', 'alice.smith@example.com', 'bob.brown@example.com'],
    'age': [23, 45, 67, 34]
}

df = pd.DataFrame(data)
print("Original Data:")
print(df)
print('\n')

# masking function 
def mask_column(df, column, mask_char='*', start=1, end=None):
    df[column] = df[column].apply(lambda x: x[:start] + mask_char * (len(x[start:end]) if end else len(x[start:])) + (x[end:] if end else ''))
    return df

# categorization function
def categorize_column(df, column, bins, labels):
    df[column] = pd.cut(df[column], bins=bins, labels=labels)
    return df

# encryption function
def encrypt_column(df, column, hash_function='sha256'):
    hash_func = getattr(hashlib, hash_function)
    df[column] = df[column].apply(lambda x: hash_func(x.encode()).hexdigest())
    return df



# 비식별화 적용
masked_df = mask_column(df.copy(), 'email', start=3, end=8)
categorized_df = categorize_column(df.copy(), 'age', bins=[0, 30, 50, 100], labels=['청년', '중년', '노년'])
encrypted_df = encrypt_column(df.copy(), 'name')

# 결과 출력
print("\nMasked Data (Email):")
print(masked_df)

print("\nCategorized Data (Age):")
print(categorized_df)

print("\nEncrypted Data (Name):")
print(encrypted_df)

# 모든 비식별화 기법을 적용한 데이터프레임
final_df = df.copy()
final_df = mask_column(final_df, 'email', start=3, end=8)
final_df = categorize_column(final_df, 'age', bins=[0, 30, 50, 100], labels=['청년', '중년', '노년'])
final_df = encrypt_column(final_df, 'name')

print("\nFinal De-identified Data:")
print(final_df)
