import sys
from collections import Counter
from io import StringIO

def main():
    
    data = sys.stdin.read().split()
    if not data:
        # 입력이 비어 있으면 아무 것도 하지 않고 종료
        return

    # 1) 첫 번째 토큰은 N (사실 사용하지 않아도 됩니다)
    n = int(data[0])

    # 2) 나머지는 N개의 정수
    nums = list(map(int, data[1:]))

    # 3) 등장 횟수 세기
    freq = Counter(nums)

    # 4) 정렬: (빈도 내림차순, 숫자 오름차순)
    #    key 함수가 (-count, num) 이므로
    #    count가 큰 순서, 같은 count 내에서는 num이 작은 순서로 정렬됩니다.
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))

    # 5) 결과 출력
    for num, count in sorted_items:
        print(num, count)

if __name__ == "__main__":
    # 테스트용 입력
    test_input = """10
    5 3 5 2 3 5 1 2 3 1
    """

    # sys.stdin을 StringIO로 대체
    sys.stdin = StringIO(test_input)

    # main() 호출 → stdout으로 결과가 바로 찍힙니다
    main()
