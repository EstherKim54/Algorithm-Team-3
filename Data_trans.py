# Json to Dict 코드
import json
import os
import pandas as pd
###

def load_json_file(filepath):
    """
    어떤 JSON 파일이든 로딩해서 딕셔너리 또는 리스트로 변환하는 함수.
    - 입력: JSON 파일 경로
    - 출력: 파이썬 dict 또는 list
    """
    if not os.path.exists(filepath):
        print(f"❌ 파일을 찾을 수 없습니다: {filepath}")
        return None

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"✅ JSON 파일 로딩 성공: {type(data).__name__}")
            return data
    except json.JSONDecodeError as e:
        print(f"❌ JSON 파싱 오류: {e}")
        return None
    except Exception as e:
        print(f"❌ 알 수 없는 오류: {e}")
        return None

# DF to Dict 코드

def csv_to_dict(filepath):
    """
    CSV 파일을 딕셔너리 리스트 형태로 변환
    - 각 행은 하나의 딕셔너리로 변환됨
    """
    try:
        df = pd.read_csv(filepath)
        return df.to_dict(orient='records')  # [{"col1": val1, ...}, ...]
    except Exception as e:
        print(f"❌ CSV 변환 실패: {e}")
        return None
