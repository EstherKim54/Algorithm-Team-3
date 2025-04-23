#!/usr/bin/env python3
from datetime import datetime
import math
import statistics

def sort_by_date(data: list[dict]) -> list[dict]:
    """
    날짜(date) 필드를 datetime으로 파싱해 오름차순 정렬
    """
    return sorted(
        data,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d')
    )

def remove_missing(data: list[dict], fields: list[str]) -> list[dict]:
    """
    지정한 필드 중 하나라도 None 또는 '' 이면 해당 항목 제거
    """
    result = []
    for item in data:
        if all(item.get(f) not in (None, '') for f in fields):
            result.append(item)
    return result

def filter_outliers(data: list[dict], field: str) -> list[dict]:
    """
    IQR(사분위수 간 범위) 방식으로 이상치를 제거.
    1) Q1, Q3 계산
    2) IQR = Q3 - Q1
    3) 허용 범위 = [Q1 - 1.5*IQR, Q3 + 1.5*IQR]
    """
    # 숫자형 값만 추출하여 정렬
    values = sorted(
        v for v in (item.get(field) for item in data)
        if isinstance(v, (int, float))
    )
    q1, _, q3 = statistics.quantiles(values, n=4, method='inclusive')
    iqr = q3 - q1
    low, high = q1 - 1.5*iqr, q3 + 1.5*iqr
    
    return [
        item for item in data
        if isinstance(item.get(field), (int, float))
           and low <= item[field] <= high
    ]

def remove_duplicates(data: list[dict], key_field: str) -> list[dict]:
    """
    key_field 기준으로 첫 등장만 남기고 중복 제거.
    (시간순 정렬 후 적용하면 가장 이른 항목만 보존)
    """
    seen, result = set(), []
    for item in data:
        key = item.get(key_field)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result

def get_oldest_entry(data: list[dict]) -> dict | None:
    """
    정렬된 리스트의 첫 번째(가장 오래된) 항목 반환. 비어 있으면 None.
    """
    return data[0] if data else None

def preprocess_data(
    data: list[dict],
    key_field: str = 'name',
    date_field: str = 'date',
    value_field: str = 'score'
) -> dict:
    """
    1) 누락값 제거
    2) 시간순 정렬
    3) 이상치 제거
    4) 중복 제거
    5) 가장 오래된 항목 추출
    """
    cleaned       = remove_missing(data,       [date_field, value_field])
    sorted_by_date= sort_by_date(cleaned)
    no_outliers   = filter_outliers(sorted_by_date, value_field)
    deduped       = remove_duplicates(no_outliers,  key_field)
    oldest        = get_oldest_entry(deduped)

    return {
        'cleaned': cleaned,
        'sorted':  sorted_by_date,
        'no_outliers': no_outliers,
        'deduped': deduped,
        'oldest':  oldest
    }

def main():
    data = [
        {"name": "홍길동", "date": "2023-11-01", "score": 88},
        {"name": "김철수", "date": "2023-10-21", "score": 75},
        {"name": "홍길동", "date": "2023-11-15", "score": 91},  # 중복
        {"name": "이영희", "date": "2023-08-09", "score": 95},
        {"name": "박영수", "date": "2023-09-30", "score": None},  # 누락
        {"name": "최민수", "date": "2023-12-01", "score": 10000}, # 이상치
    ]

    result = preprocess_data(data)
    # …전처리 수행까지는 동일…

    print("===============================")
    print(" 🤖 데이터 전처리 결과")
    print("===============================")
    print(f"원본 데이터:      {len(data)}건")
    print(f"누락값 제거 후:   {len(result['cleaned'])}건")
    print(f"이상치 제거 후:   {len(result['no_outliers'])}건")
    print(f"중복 제거 후:     {len(result['deduped'])}건\n")

    # 1) 누락값 제거 후 정렬
    print("1) 누락값 제거 → 시간순 정렬 결과:")
    for item in result['sorted']:
        print(f"- {item['date']} | {item['name']} | {item['score']}점")

    # 2) 이상치 제거 후 정렬
    print("\n2) 이상치 제거 → 시간순 정렬 결과:")
    for item in result['no_outliers']:
        print(f"- {item['date']} | {item['name']} | {item['score']}점")

    # 3) 중복 제거 후 정렬 (최종)
    print("\n3) 중복 제거 → 최종 시간순 정렬 결과:")
    for item in result['deduped']:
        print(f"- {item['date']} | {item['name']} | {item['score']}점")

    # 가장 오래된 항목
    if result['oldest']:
        o = result['oldest']
        print(f"\n가장 오래된 항목: {o['name']} ({o['date']})")

if __name__ == "__main__":
    main()

# 수정 테스트