# 문제 2: 이진 탐색 기반 탐지

# · 내용: 정렬된 리스트에서 특정 값을 이진 탐색으로 찾기

# · 준비: 반복형/재귀형 이진 탐색 구현, 성공/실패 결과 반환 처리

# · 비고: YES/NO 출력 형식에 유의

import json
import os
import pandas as pd

# 반복형 이진 탐색 구현 (key 함수 사용 가능)
def binary_search_iterative(arr, target, key=lambda x: x):
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

# 재귀형 이진 탐색 구현 (key 함수 사용 가능)
def binary_search_recursive(arr, target, left, right, key=lambda x: x):
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

# 딕셔너리 리스트 대상 이진 탐색 실행 함수
def solve_problem_2(arr, target, key_name=None):
    # 단순 리스트일 경우
    if key_name is None:
        print("📋 검색 대상 리스트 (원소 자체 비교):")
        print(arr)

        result_iter = binary_search_iterative(arr, target)
        result_rec  = binary_search_recursive(arr, target, 0, len(arr) - 1)

    # 딕셔너리 리스트일 경우 (key 기준 비교)
    else:
        # 원본 출력 (정렬 여부는 호출 측에 맡김)
        print(f"📋 검색 대상 리스트 ({key_name} 기준 정렬):")
        for item in arr:
            print(item)

        result_iter = binary_search_iterative(arr, target, key=lambda x: x[key_name])
        result_rec  = binary_search_recursive(arr, target, 0, len(arr) - 1, key=lambda x: x[key_name])

    # 최종 결과 출력
    print(f"▶ 반복형 결과: {result_iter}")
    print(f"▶ 재귀형 결과: {result_rec}")

