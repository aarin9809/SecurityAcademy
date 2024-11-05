import pandas as pd
import argparse

# 비식별화 함수
def de_identify(df, column_name, deid_option):
    # 옵션 1: 첫 몇 글자를 마스킹 (간단한 예)
    if deid_option == 1:
        df[column_name] = df[column_name].apply(lambda x: x[:2] + '*' * (len(x) - 2) if isinstance(x, str) else x)
        # x = df[column_name]에 해당함.
        # if isinstance(x, str) : x가 문자열인지 확인함
        # 만약 x가 문자열이라면, x[:2]는 문자열의 처음 두 글자를 가져온다.
        # '*' * (len(x) - 2)는 나머지 글자 수만큼 *로 채운다. 예를 들어, 문자열의 길이가 5라면 3개의 *가 추가된다.
        # 마지막으로 x가 문자열이 아닌 경우에는 그대로 반환한다.
        # ex) 이름이 '홍길동' 이라면 비식별화 된 결과는 홍*동으로 표시된다.

    # 옵션 2: 해시값으로 대체
    elif deid_option == 2:
        df[column_name] = df[column_name].apply(lambda x: hash(x) if isinstance(x, str) else x)

    # 옵션 3: 해당 컬럼을 제거
    elif deid_option == 3:
        df.drop(column_name, axis=1, inplace=True)
    else:
        raise ValueError("잘못된 de_id 옵션")
    return df

def main(input_path, deid_option, column_name, output_path):
    # CSV 파일 로드
    df = pd.read_csv(input_path, encoding='cp949')
    
    # 비식별화 수행
    df = de_identify(df, column_name, deid_option)
    
    # 결과 CSV 파일로 저장
    df.to_csv(output_path, index=False, encoding='cp949')
    print(f"처리된 파일이 {output_path}에 저장되었습니다.")

if __name__ == "__main__":
    # 명령줄 인자 처리
    parser = argparse.ArgumentParser(description="CSV 비식별화 스크립트")
    
    parser.add_argument('--input_path', type=str, required=True, help="입력 CSV 파일 경로") # CSV 파일 위치 입력
    parser.add_argument('--deid', type=int, required=True, choices=[1, 2, 3], help="비식별 옵션 (1: 마스킹, 2: 해시, 3: 컬럼 제거)")    # 비식별 옵션 입력
    parser.add_argument('--column_name', type=str, required=True, help="비식별할 컬럼명")   # 비식별화 할 컬럼명 입력
    parser.add_argument('--output_path', type=str, required=True, help="출력 CSV 파일 경로")    # 비식별화가 완료된 파일명과 위치를 입력하는 옵션
    
    args = parser.parse_args()
    
    # 메인 함수 호출
    main(args.input_path, args.deid, args.column_name, args.output_path)
