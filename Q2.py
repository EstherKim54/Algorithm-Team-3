# 문제 2: 이진 탐색 기반 탐지

# · 내용: 정렬된 리스트에서 특정 값을 이진 탐색으로 찾기

# · 준비: 반복형/재귀형 이진 탐색 구현, 성공/실패 결과 반환 처리

# · 비고: YES/NO 출력 형식에 유의

# 강아지

import json
import os
import pandas as pd

# 이진탐색 구현 (반복)
def binary_search_iterative(arr, target, key=lambda x: x):
    """ 반복형 이진 탐색 (key 지원)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        value = key(arr[mid])
        if value == target:
            return "YES"
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1
    return "NO"

# 이진탐색 구현 (재귀)
def binary_search_recursive(arr, target, left, right, key=lambda x: x):
    """ 재귀형 이진 탐색 (key 지원)"""
    if left > right:
        return "NO"
    mid = (left + right) // 2
    value = key(arr[mid])
    if value == target:
        return "YES"
    elif value < target:
        return binary_search_recursive(arr, target, mid + 1, right, key)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, key)


# 리스트를 인자로 받아서 탐색
def solve_list_problem_2(arr, target):
    """
    arr    : 정렬된 리스트 (숫자 또는 문자열)
    target : 탐색할 값
    """
    # 원본 리스트 출력
    print("📋 검색 대상 리스트:")
    print(arr)

    # 반복형 이분 탐색
    result_iter = binary_search_iterative(arr, target)
    # 재귀형 이분 탐색
    result_rec = binary_search_recursive(arr, target, 0, len(arr) - 1)

    # 결과 출력
    print(f"▶ 반복형 결과: {result_iter}")
    print(f"▶ 재귀형 결과: {result_rec}")

# 딕셔너리를 인자로 받아서 탐색
def solve_dict_problem_2(arr, target, key_name=None):
    """
    arr      : 정렬된 리스트. 요소가 숫자/문자열인지, dict인지 자동 감지.
    target   : 탐색할 값
    key_name : dict 요소를 탐색할 때 사용할 키 (예: "score" or "name").
               기본 None 이면 숫자/문자열 리스트 모드로 간주.
    """
    # --- 리스트 모드 ---
    if key_name is None:
        print("📋 검색 대상 리스트 (원소 자체 비교):")
        print(arr)

        # 반복형 이분 탐색
        result_iter = binary_search_iterative(arr, target)
        # 재귀형 이분 탐색
        result_rec  = binary_search_recursive(arr, target, 0, len(arr) - 1)

    # --- 딕셔너리 모드 ---
    else:
        # key_name 기준으로 정렬
        # arr = sorted(arr, key=lambda x: x[key_name]) # 정렬을 해주는 코드 (키를 기준으로)
        print(f"📋 검색 대상 리스트 ({key_name} 기준 정렬):")
        for item in arr:
            print(item)

        # 반복형 이분 탐색 (key 지원)
        result_iter = binary_search_iterative(arr, target, key=lambda x: x[key_name])
        # 재귀형 이분 탐색
        result_rec  = binary_search_recursive(arr, target, 0, len(arr) - 1, key=lambda x: x[key_name])

    # --- 결과 출력 ---
    print(f"▶ 반복형 결과: {result_iter}")
    print(f"▶ 재귀형 결과: {result_rec}")
