# Json to Dict 코드
import json
import os
import pandas as pd
###

### Q1 
# 딕셔너리, 리스트 무관한 코드
def bubble_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if key(arr[j]) > key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if key(arr[j]) < key(arr[min_idx]):
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr, key=lambda x: x):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key(key_item):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

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
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    pivot = key(arr[0])
    left = [x for x in arr[1:] if key(x) < pivot]
    mid = [x for x in arr if key(x) == pivot]
    right = [x for x in arr[1:] if key(x) > pivot]
    return quick_sort(left, key) + mid + quick_sort(right, key)


# List로 인자를 받은 경우
def solve_list_problem_1_(list_data):
    sort_algorithms = {
        "1": ("버블 정렬", bubble_sort),
        "2": ("선택 정렬", selection_sort),
        "3": ("삽입 정렬", insertion_sort),
        "4": ("병합 정렬", merge_sort),
        "5": ("퀵 정렬", quick_sort),
    }

    print("정렬 알고리즘 선택:")
    for k, (name, _) in sort_algorithms.items():
        print(f"{k}. {name}")
    algo_choice = input("번호 선택: ").strip()

    if algo_choice not in sort_algorithms:
        print("❌ 잘못된 번호입니다.")
        return

    algo_name, sort_func = sort_algorithms[algo_choice]

    print(f"\n📋 원본 리스트:")
    print(list_data)

    sorted_arr = sort_func(list_data.copy())

    print(f"\n✅ {algo_name} 결과:")
    print(sorted_arr)

# 딕셔너리로 인자를 받은 경우
def solve_dict_problem_1_(dict_data, sort_key):
    sort_algorithms = {
        "1": ("버블 정렬", bubble_sort),
        "2": ("선택 정렬", selection_sort),
        "3": ("삽입 정렬", insertion_sort),
        "4": ("병합 정렬", merge_sort),
        "5": ("퀵 정렬", quick_sort),
    }

    print("정렬 알고리즘 선택:")
    for k, (name, _) in sort_algorithms.items():
        print(f"{k}. {name}")
    algo_choice = input("번호 선택: ").strip()

    if algo_choice not in sort_algorithms:
        print("❌ 잘못된 번호입니다.")
        return

    algo_name, sort_func = sort_algorithms[algo_choice]

    print(f"\n📋 원본 딕셔너리 리스트:")
    for item in dict_data:
        print(item)

    sorted_arr = sort_func(dict_data.copy(), key=lambda x: x[sort_key])

    print(f"\n✅ {algo_name} 결과 ({sort_key} 기준 정렬):")
    for item in sorted_arr:
        print(item)
