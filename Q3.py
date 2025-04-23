from collections import Counter
import random

# 1) 리스트 파일 일 경우 예) [5,3,5,2]

def frequency_sort(nums: list[int]) -> list[tuple[int,int]]:
    # 예: nums = [5,3,5,2] ->  freq = {5:2, 3:1, 2:1}
    freq = Counter(nums)

    # 정렬: (빈도 내림차순, 숫자 내림차순)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
    
    return sorted_items
if __name__ == "__main__":
  nums = [random.randint(1, 10) for _ in range(100)]
  print("입력 리스트 (100개 랜덤 정수):", nums)

  result = frequency_sort(nums)
  
   # 결과 출력
  print("빈도 내림차순, 숫자 내림차순 정렬 결과:")
  for num, count in result:
      print(num, count)





# ------------------------------------------------------
# 2) 딕셔너리 파일 일 경우 예) {"user": "홍길동", "score": 88}
def frequency_sort_records(records: list[dict]) -> list[tuple[int,int]]:
    
    # score 필드가 있는 레코드 중 None이 아닌 값만 리스트로 추출
    scores = [rec['score'] for rec in records if rec.get('score') is not None]

    # 등장 횟수 세기
    freq = Counter(scores)

    # 정렬: 빈도 내림차순, 점수 내림차순
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
    return sorted_items

if __name__ == "__main__":
    records = [
        {"name": f"user{i+1}", "score": random.randint(1, 100)}
        for i in range(30)
    ]

    for rec in records:
        print(rec)

    # 정렬된 결과 얻기
    result = frequency_sort_records(records)

    # 결과 출력
    print("\n점수 빈도 내림차순, 점수 내림차순 정렬 결과:")
    for score, count in result:
        print(f"Score: {score}, Count: {count}")





# ------------------------------------------------------
# 3) 딕셔너리에서 전처리 (missing value 제거,  중복 제거, outlier 제거) 추가한 코드
from collections import Counter
import random
import statistics


def preprocess_records(records: list[dict]) -> list[dict]:
    """
    records 전처리 함수:
    1) 'score'가 없거나 None인 레코드 제거
    2) 동일한 ('name', 'score') 조합의 중복 레코드는 첫 등장만 보존
    3) IQR(Interquartile Range) 기법을 이용해 이상치 제거

    :param records: 원본 레코드 리스트
    :return: 전처리된 레코드 리스트
    """
    # 1) 결측값 제거
    filtered = [r for r in records if r.get('score') is not None]

    # 2) 중복 제거 (name, score 기반)
    seen = set()
    unique = []
    for r in filtered:
        key = (r.get('name'), r.get('score'))
        if key not in seen:
            seen.add(key)
            unique.append(r)

    # 3) 이상치 제거 (IQR 기반)
    scores = [r['score'] for r in unique]
    if len(scores) < 4:
        return unique
    q1, _, q3 = statistics.quantiles(scores, n=4, method='inclusive')
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    cleaned = [r for r in unique if lower <= r['score'] <= upper]

    return cleaned


def frequency_sort_records(records: list[dict]) -> list[tuple[int, int]]:
    """
    전처리된 records에서 'score' 값의 빈도수를 계산하여
    빈도수 내림차순, 점수 내림차순으로 정렬된 (score, count) 리스트 반환
    """
    processed = preprocess_records(records)
    scores = [r['score'] for r in processed]
    freq = Counter(scores)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
    return sorted_items


if __name__ == "__main__":
    # 예시 데이터: name과 score 필드만 포함된 레코드
    records = [
        {"name": "홍길동", "score": 88},
        {"name": "김철수", "score": 75},
        {"name": "홍길동", "score": 88},  # 중복 제거 확인용
        {"name": "이영희", "score": 95},
        {"name": "박영수", "score": None},  # 누락
        {"name": "최민수", "score": 10000}, # 이상치
        *[
            {"name": f"사용자{i+1}", "score": random.randint(1, 100)}
            for i in range(10)
        ]
    ]

    print("원본 레코드 (중복·결측·이상치 포함):")
    for rec in records:
        print(rec)

    # 전처리 단계 결과 확인
    processed = preprocess_records(records)
    print("\n전처리된 레코드 (중복·결측·이상치 제거 후):")
    for rec in processed:
        print(rec)

    # 점수 빈도 정렬 결과
    result = frequency_sort_records(records)
    print("\n전처리 후 점수 빈도 내림차순, 점수 내림차순 정렬 결과:")
    for score, count in result:
        print(f"Score: {score}, Count: {count}")
