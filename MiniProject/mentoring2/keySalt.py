import pandas as pd
import hashlib

# SHA256 암호화 함수 정의
def encrypt_data_sha256(data):
    sha_signature = hashlib.sha256(data.encode()).hexdigest()
    return sha_signature

# 파일 경로 설정
file1_path = './key_index_to_csv.csv'
file2_path = './key_index_to_csv1.csv'
output_path = './sha256_merged_file.csv'

# chunk 단위로 데이터를 읽어서 처리 및 암호화
chunk_size = 1000
with pd.read_csv(file1_path, chunksize=chunk_size) as reader1, \
     pd.read_csv(file2_path, chunksize=chunk_size) as reader2:
    
    merged_chunks = []
    
    for chunk1, chunk2 in zip(reader1, reader2):
        # 'name' 열을 SHA256으로 암호화
        chunk1['name'] = chunk1['name'].apply(encrypt_data_sha256)
        chunk2['name'] = chunk2['name'].apply(encrypt_data_sha256)
        
        # 두 chunk를 합치기
        merged_chunk = pd.concat([chunk1, chunk2])
        merged_chunks.append(merged_chunk)

    # 전체를 하나의 데이터프레임으로 결합
    final_df = pd.concat(merged_chunks)

# 결과를 CSV 파일로 저장
final_df.to_csv(output_path, index=False)

print(f"파일이 성공적으로 병합되어 저장되었습니다: {output_path}")
