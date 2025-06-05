import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Kaggle 인증 경로 설정
os.environ['KAGGLE_CONFIG_DIR'] = os.path.expanduser('~/.kaggle')

# API 객체 생성 및 인증
api = KaggleApi()
api.authenticate()

# 데이터 다운로드
api.dataset_download_files(
    'ramamet4/app-store-apple-data-set-10k-apps',
    path='data',
    unzip=True
)

print("✅ 다운로드 완료! 'data' 폴더를 확인하세요.")
