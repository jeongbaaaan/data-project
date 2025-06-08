# pandas는 데이터 분석할 때 제일 많이 쓰이는 라이브러리예요
import pandas as pd

# 데이터 파일 경로가 정확해야 불러올 수 있어요. 경로 틀리면 FileNotFoundError 납니다.
# 현재 폴더 구조 기준으로 이 경로가 맞다면 그대로 사용하면 돼요
file_path = "data/data/AppleStore.csv"

# CSV 파일 읽어오기
df = pd.read_csv(file_path)

# 데이터가 잘 들어왔는지 확인: 행(row) 수, 열(column) 수
print("✅ 데이터 크기 (행, 열):", df.shape)

# 데이터 맨 위 5개 행만 보기 (전체 출력은 너무 길어요)
print("\n📌 데이터 상위 5개:")
print(df.head())

# 어떤 컬럼들이 있는지 전체 이름 출력
print("\n🧾 컬럼 목록:")
print(df.columns.tolist())

# 혹시 비어있는 데이터는 없는지 확인 (비어 있으면 분석 전에 처리해야 해요)
print("\n🚨 컬럼별 결측치 개수:")
print(df.isnull().sum())

# 수치형 데이터는 평균, 표준편차 등 요약 통계 정보도 볼 수 있어요
print("\n📊 수치형 컬럼 통계 요약:")
print(df.describe())
