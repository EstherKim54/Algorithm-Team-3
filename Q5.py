import time
import matplotlib.pyplot as plt

#정렬 알고리즘 나열하기

#Quicksort 알고리즘

def quick_sort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [x for x in data[1:] if x <= pivot]
    right = [x for x in data[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

#---------------------------------------------------------------------------------

#Timsort(직접 구현) 알고리즘

MIN_MERGE = 32

def insert_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def fast_merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def tim_sort(arr):
    def calc_min_run(n):
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1
            n >>= 1
        return n + r

    n = len(arr)
    min_run = calc_min_run(n)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insert_sort(arr, start, end)

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            mid = min(n - 1, start + size - 1)
            right = min(start + 2 * size - 1, n - 1)
            if mid < right:
                merged = fast_merge(arr[start:mid+1], arr[mid+1:right+1])
                arr[start:start + len(merged)] = merged
        size *= 2
    return arr

# ---------------------------------------------------------------------------------------

#파일 읽어오는 함수
def read_integers(filepath):
    with open(filepath, 'r') as f:
        numbers = []
        for line in f:
            parts = line.strip().split()
            numbers.extend(int(x) for x in parts if x.strip())
    return numbers

#각 알고리즘마다 걸리는 시간 구하는 함수
def sort_and_measure(name, sort_fn, numbers, result_dict):
    data = numbers.copy()
    start_time = time.time()
    sort_fn(data)
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"{name:<25}: {elapsed:.2f}초")
    result_dict[name] = elapsed

# ---------------------------------------------------------------------------------------

#시각화 하는 함수 (막대그래프로 그리기)
def visualize_results(results):
    names = list(results.keys())
    times = list(results.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, times, color='skyblue')
    for bar, t in zip(bars, times):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f"{t:.2f}s", ha='center', va='bottom')
    
    plt.title("정렬 알고리즘 실행 시간 비교")
    plt.ylabel("시간 (초)")
    plt.xticks(rotation=15)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

# ---------------------------------------------------------------------------------------

#메인 함수 만들어서 (시간 출력하기)
def main():
    filepath = "random_1M_integers.txt"
    numbers = read_integers(filepath)

    results = {}

    #각 정렬마다 걸리는 시간 출력
    sort_and_measure("Function sort()", lambda x: x.sort(), numbers, results)       #내장함수기 때문에 바로 내장함수 사용
    sort_and_measure("Quick Sort", quick_sort, numbers, results)
    sort_and_measure("Tim Sort", tim_sort, numbers, results)

    #막대그래프 시각화하기
    visualize_results(results)

if __name__ == "__main__":
    main()
