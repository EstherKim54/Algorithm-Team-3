import json
import os
import pandas as pd

# 정렬 알고리즘 구현부 (공통 key 사용 가능)

# 버블 정렬: 인접한 요소를 반복적으로 비교하며 정렬
def bubble_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 선택 정렬: 가장 작은 값을 찾아 앞으로 이동
def selection_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 삽입 정렬: 현재 요소를 앞쪽 정렬된 부분에 적절히 삽입
def insertion_sort(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key(key_item):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# 병합 정렬: 배열을 절반씩 나눈 후 병합하여 정렬
def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

# 병합 로직 (merge_sort에서 사용)
def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 퀵 정렬: 기준값을 중심으로 좌우 분할 후 재귀 정렬
def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = key(arr[0])
    left = [x for x in arr[1:] if key(x) < pivot]
    mid = [x for x in arr if key(x) == pivot]
    right = [x for x in arr[1:] if key(x) > pivot]
    return quick_sort(left, key) + mid + quick_sort(right, key)

# 리스트 데이터를 입력받아 정렬하는 함수
def solve_list_problem_1_(list_data):
    sort_algorithms = {
        "1": ("버블 정렬", bubble_sort),
        "2": ("선택 정렬", selection_sort),
        "3": ("삽입 정렬", insertion_sort),
        "4": ("병합 정렬", merge_sort),
        "5": ("퀵 정렬", quick_sort),
    }

    # 사용자에게 정렬 방식 선택 요청
    print("정렬 알고리즘 선택:")
    for k, (name, _) in sort_algorithms.items():
        print(f"{k}. {name}")
    algo_choice = input("번호 선택: ").strip()

    # 잘못된 입력 처리
    if algo_choice not in sort_algorithms:
        print("잘못된 번호입니다.")
        return

    algo_name, sort_func = sort_algorithms[algo_choice]

    # 정렬 전 리스트 출력
    print("\n원본 리스트:")
    print(list_data)

    # 정렬 수행
    sorted_arr = sort_func(list_data.copy())

    # 정렬 결과 출력
    print(f"\n{algo_name} 결과:")
    print(sorted_arr)

# 리스트 또는 딕셔너리 리스트를 정렬하는 함수
# data: 정렬 대상 데이터 (리스트 또는 딕셔너리 리스트)
# key_name: 딕셔너리 리스트인 경우 정렬 기준이 되는 키 이름 (None이면 일반 리스트로 처리)
def solve_problem_1(data, key_name=None):
    # 사용 가능한 정렬 알고리즘을 딕셔너리로 정의
    # 키: 사용자 입력값 (문자열), 값: (알고리즘 이름, 알고리즘 함수)
    sort_algorithms = {
        "1": ("버블 정렬", bubble_sort),
        "2": ("선택 정렬", selection_sort),
        "3": ("삽입 정렬", insertion_sort),
        "4": ("병합 정렬", merge_sort),
        "5": ("퀵 정렬", quick_sort),
    }

    # 사용자에게 정렬 알고리즘 선택을 안내
    print("정렬 알고리즘 선택:")
    for k, (name, _) in sort_algorithms.items():
        print(f"{k}. {name}")

    # 사용자 입력을 받아 선택한 알고리즘 결정
    algo_choice = input("번호 선택: ").strip()

    # 입력값 검증: 선택이 잘못된 경우 함수 종료
    if algo_choice not in sort_algorithms:
        print("잘못된 번호입니다.")
        return

    # 선택한 알고리즘 이름과 정렬 함수 가져오기
    algo_name, sort_func = sort_algorithms[algo_choice]

    # 일반 리스트일 경우 (key_name이 없는 경우)
    if key_name is None:
        print("\n📋 원본 리스트:")
        print(data)

        # 정렬 함수 호출 (원본을 복사해서 정렬)
        sorted_arr = sort_func(data.copy())

        # 정렬 결과 출력
        print(f"\n✅ {algo_name} 결과:")
        print(sorted_arr)

    # 딕셔너리 리스트일 경우 (key_name 기준으로 정렬)
    else:
        print(f"\n📋 원본 딕셔너리 리스트 ({key_name} 기준):")
        for item in data:
            print(item)

        # 정렬 함수 호출 (key 매개변수로 정렬 기준 함수 전달)
        sorted_arr = sort_func(data.copy(), key=lambda x: x[key_name])

        # 정렬 결과 출력
        print(f"\n✅ {algo_name} 결과 ({key_name} 기준 정렬):")
        for item in sorted_arr:
            print(item)

# 모든 정렬 알고리즘을 사용하여 결과를 출력하는 함수
def solve_problem_1_all(data, key_name=None):
    sort_algorithms = {
        "1": ("버블 정렬", bubble_sort),
        "2": ("선택 정렬", selection_sort),
        "3": ("삽입 정렬", insertion_sort),
        "4": ("병합 정렬", merge_sort),
        "5": ("퀵 정렬", quick_sort),
    }

    print("📋 원본 데이터:")
    if key_name is None: # 키가 없으면 리스트로 
        print(data) 
    else: # 키가 있다면 딕셔너리 형태
        for item in data:
            print(item)

    print("\n📊 모든 정렬 결과:")
    for algo_key, (algo_name, sort_func) in sort_algorithms.items():
        print(f"\n🔹 {algo_name} 결과:")
        if key_name is None:
            sorted_arr = sort_func(data.copy())
            print(sorted_arr)
        else:
            sorted_arr = sort_func(data.copy(), key=lambda x: x[key_name])
            for item in sorted_arr:
                print(item)
