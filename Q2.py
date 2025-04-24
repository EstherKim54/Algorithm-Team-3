lst = [31, -36, -47, 44, -15, -19, -22, -33, 44, -37, 36, 44, 19, -39, 25, 4, -46, -47, -39, -23,
 -21, 14, 27, -47, 21, -25, 41, 33, 39, 19, 3, -22, 7, 25, -15, -50, 47, -30, 39, 4,
 -7, -15, -31, -23, 47, -7, -37, -39, -2, -38, -5, -6, 27, -17, -45, 43, 8, 18, -35, -2,
 -40, 20, -13, 30, 29, -4, 23, -26, 40, -42, -45, 34, -21, 48, -13, -40, -21, -38, -2, -15,
 8, 31, -4, -30, -3, -5, -24, 35, -16, 39, 37, 32, -41, 27, 31, -29, 18, 43, -19, -30]

def find_target_indices(lst, target):
    lst = sorted(lst)  # 이진 탐색을 위해 정렬
    left, right = 0, len(lst) - 1 # left right 설정
    found = False # 기존 설정값은 False
    
    # 이진 탐색으로 target 존재 여부 확인
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            found = True
            break
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Target이 없다면 출력할 문구
    if not found:
        print("Not Found")
        return

    # 정렬된 리스트에서 target의 모든 인덱스 찾기
    indices = [i for i, val in enumerate(lst) if val == target]
    print(indices) # 위치 리스트 출력
    print(indices[0] + indices[-1]) # 첫+마지막 인덱스 합 출력

find_target_indices(lst,-15)  # lst리스트와 타겟변수를 활용하여 문제 풀이


