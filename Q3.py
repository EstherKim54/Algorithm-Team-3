from collections import Counter

def frequency_sort(nums: list[int]) -> list[tuple[int,int]]:
    # 1) Counter 클래스로 nums 안 숫자들의 등장 횟수를 센다.
    #    예: nums = [5,3,5,2] → Counter({5:2, 3:1, 2:1})
    freq = Counter(nums)

    # 2) freq.items() = [(5,2), (3,1), (2,1)] 형태의 리스트를 가져온 다음,
    #    sorted()로 '(-횟수, -숫자)' 기준 정렬.
    #    여기서 -를 붙이면 내림차순이 된다.
    #    → 횟수 큰 순, 횟수 같으면 숫자 큰 순
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
    
    # 3) 정렬된 (숫자,횟수) 리스트 반환
    return sorted_items

if __name__ == "__main__":
    nums = [
    5, 2, 4, 3, 9, 0, 4, 1, 3, 5,
    6, 8, 4, 2, 7, 6, 0, 9, 3, 5,
    2, 1, 4, 7, 8, 2, 9, 3, 5, 0,
    1, 1, 6, 5, 4, 4, 3, 9, 2, 2,
    8, 7, 0, 6, 5, 5, 3, 4, 1, 2,
    0, 0, 9, 9, 6, 3, 2, 4, 7, 8,
    5, 1, 1, 0, 0, 6, 8, 9, 2, 3,
    5, 7, 4, 0, 1, 2, 8, 5, 6, 3,
    9, 0, 4, 2, 3, 1, 7, 6, 5, 4,
    8, 9, 0, 2, 1, 3, 5, 4, 6, 7]


    print(nums)

    # 5) 함수 호출
    result = frequency_sort(nums)
    print(result)

    # 6) 결과 출력
    print(result[0][0])
    print(result[0][1])
    passcord = result[0][0] + result[0][1]
    print(passcord)