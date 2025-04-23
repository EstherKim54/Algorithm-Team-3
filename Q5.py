import time

MIN_MERGE = 32

# 삽입 정렬
def insertSort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 병합 함수
def fastmerge(array1, array2):
    merged = []
    i = j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1
    merged.extend(array1[i:])
    merged.extend(array2[j:])
    return merged

# Timsort 본체
def timSort(arr):
    def calcMinRun(n):
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1      #n이 홀수면 1, 짝수면 0 (binary 연산)
            n >>= 1
        return n + r

    n = len(arr)
    minRun = calcMinRun(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertSort(arr, start, end)

    currentSize = minRun
    while currentSize < n:
        for start in range(0, n, currentSize * 2):
            mid = min(n - 1, start + currentSize - 1)
            right = min(start + 2 * currentSize - 1, n - 1)
            if mid < right:
                merged = fastmerge(arr[start:mid + 1], arr[mid + 1:right + 1])
                arr[start:start + len(merged)] = merged
        currentSize *= 2

    return arr

# 메인 함수
def main():
    file_path = "random_1M_integers.txt"

    start_time = time.time()

    with open(file_path, "r") as file:
        content = file.read().split()
        n = int(content[0])
        numbers = list(map(int, content[1:]))

    read_time = time.time()

    sorted_numbers = timSort(numbers)

    sort_time = time.time()

    #print("정렬된 리스트:", sorted_numbers)
    print(f"파일 읽는 시간: {read_time - start_time:.2f}초")
    print(f"Timsort 정렬 시간: {sort_time - read_time:.2f}초")
    print(f"총 실행 시간: {sort_time - start_time:.2f}초")

if __name__ == "__main__":
    main()
