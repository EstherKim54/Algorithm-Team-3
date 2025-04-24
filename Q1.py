
### Solv
shuffled_list = [
    "-900", "3", "baz", "six^", "2", "65", "comma,", "0", "adipiscing", "-500",
    "space ", "foo", "15", "75", "-100", "10", "one!", "lorem", "one", "-600",
    "-450", "bar", "world", "five%", "star*", "ten", "four$", "500", "95", "thousand",
    "300", "-50", "-25", "70", "minus", "xyz", "-200", "abc!", "do", "-888",
    "35", "incididunt", "400", "7", "700", "-20", "100", "500", "100", "hello",
    "3a", "55", "three#", "-350", "-10", "five", "4", "-4", "-700", "2",
    "abc", "xyz", "-250", "2", "zero", "-650", "-15", "ten)", "consectetur", "-1",
    "45", "eight*", "elit", "-77", "-50", "ten", "0", "underscore_", "four", "-100",
    "-300", "-10", "40", "-850", "seven&", "700", "-200", "amet", "-25", "1",
    "33", "85", "dolore", "nine(", "99", "dolor", "6", "-999", "3", "baz",
    "lorem", "six^", "bar", "seven&", "100", "xyz", "two@", "adipiscing", "-200", "abc!",
    "-1000", "nine(", "5", "-850", "consectetur", "999", "bar", "xyz", "-700", "999",
    "foo", "plus", "70", "-900", "-20", "-250", "incididunt", "three#", "one!", "hello",
    "six^", "1", "-777", "abc", "comma,", "cat", "bar", "baz", "baz", "3a",
    "abc123", "-500", "7", "-650", "-300", "hello", "bar", "NaN", "999", "space ",
    "999", "star*", "ten", "-450", "underscore_", "three#", "baz", "five", "-100", "-1000",
    "-100", "baz", "one", "1.5", "nine(", "-15", "five%", "5", "six^", "-300",
    "consectetur", "-100", "cat", "eight*", "baz", "baz", "space ", "baz", "baz", "baz"
]

# 문자를 숫자로 바꿈, 에러가나는 경우를 빼고
processed_list = []
for item in shuffled_list:
    try:
        # 숫자로 변환 가능한 경우 float으로 변환 (정수든 실수든 다 커버)
        number = int(item)
        processed_list.append(number)
    except (ValueError, TypeError):
        continue

# 기존 processed_list에서 중복 제거 (순서 유지)
arr = []
seen = set()

for num in processed_list:
    if num not in seen: # set을 이용해서 처음 이후 두번쨰 만나는 값들은 모두 무시
        arr.append(num)
        seen.add(num) 

import time

# 삽입 정렬
def insertion_sort(arr, key=lambda x: x):
    start_time = time.time()

    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key(arr[j]) > key(key_item):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

    end_time = time.time()
    print(f"삽입 정렬 시간: {end_time - start_time:.6f}초")
    return arr


print(insertion_sort(arr))

# 사용한 정렬 알고리즘: 삽입정렬
# 51개의 작은 리스트 값일 경우 선택정렬이 가장 시간복잡도가 낮다. 