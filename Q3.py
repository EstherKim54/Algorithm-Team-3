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
    nums = [4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]


    print(nums)

    # 5) 함수 호출
    result = frequency_sort(nums)
    print(result)

    # 6) 결과 출력
    print(result[0][0])
    print(result[0][1])
    passcord = result[0][0] + result[0][1]
    print(passcord)