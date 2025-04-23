import json
import os
import pandas as pd

def load_json_file(filepath):
    """
    JSON 파일을 로딩하여 파이썬 객체(dict 또는 list)로 변환하는 함수.
    
    Parameters:
        filepath (str): JSON 파일의 경로

    Returns:
        dict or list or None: JSON 파일을 성공적으로 파싱한 경우 해당 객체 반환,
                              실패 시 None 반환
    """
    if not os.path.exists(filepath):
        print(f"파일을 찾을 수 없습니다: {filepath}")
        return None

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            print(f"JSON 파일 로딩 성공: {type(data).__name__}")
            return data
    except json.JSONDecodeError as e:
        print(f"JSON 파싱 오류: {e}")
        return None
    except Exception as e:
        print(f"알 수 없는 오류: {e}")
        return None

def csv_to_dict(filepath):
    """
    CSV 파일을 읽어 각 행을 딕셔너리로 변환한 리스트를 반환하는 함수.
    
    Parameters:
        filepath (str): CSV 파일 경로

    Returns:
        list of dict or None: 변환된 딕셔너리 리스트 반환. 오류 발생 시 None 반환
    """
    try:
        df = pd.read_csv(filepath)
        return df.to_dict(orient='records')  # [{"컬럼1": 값1, "컬럼2": 값2, ...}, ...]
    except Exception as e:
        print(f"CSV 변환 실패: {e}")
        return None
