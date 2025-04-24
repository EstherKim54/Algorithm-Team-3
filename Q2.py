lst = [31, -36, -47, 44, -15, -19, -22, -33, 44, -37, 36, 44, 19, -39, 25, 4, -46, -47, -39, -23,
 -21, 14, 27, -47, 21, -25, 41, 33, 39, 19, 3, -22, 7, 25, -15, -50, 47, -30, 39, 4,
 -7, -15, -31, -23, 47, -7, -37, -39, -2, -38, -5, -6, 27, -17, -45, 43, 8, 18, -35, -2,
 -40, 20, -13, 30, 29, -4, 23, -26, 40, -42, -45, 34, -21, 48, -13, -40, -21, -38, -2, -15,
 8, 31, -4, -30, -3, -5, -24, 35, -16, 39, 37, 32, -41, 27, 31, -29, 18, 43, -19, -30]

def find_target_indices(lst, target):
    lst = sorted(lst)  # 정렬
    left, right = 0, len(lst) - 1
    found = False

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            found = True
            break
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if not found:
        print("Not Found")
        return

    # 존재할 경우 인덱스 출력 및 합 계산
    indices = [i for i, val in enumerate(lst) if val == target]
    print(indices)
    print(indices[0] + indices[-1])

find_target_indices(lst,-15)

