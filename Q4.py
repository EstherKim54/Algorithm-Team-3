import random

# 격자를 size x size 크기로 생성하는 함수
# 각 셀에는 0부터 9까지의 랜덤한 정수가 들어감
def generate_grid(size):
    grid = []

    # size만큼 행 반복
    for i in range(size):
        row = []

        for j in range(size):
            number = random.randint(0, 9)  # 0~9 사이의 랜덤 숫자
            row.append(number)  # 숫자를 행에 추가

        grid.append(row)  # 완성된 행을 격자에 추가
    return grid

# 격자를 출력하는 함수
def print_grid(grid):
    # 격자의 각 행을 하나씩 꺼냄냄
    for row in grid:
        line = ""
        for num in row:
            # 각 숫자를 문자열로 변환하고 공백을 사이에 넣어 연결
            line += str(num) + " "
        print(line.strip())  # 마지막 공백 제거 후 출력

# 0을 찾고 경로를 출력하는 함수
def find_zero_with_path(grid):
    size = len(grid)
    path = []

    for i in range(size):
        for j in range(size):
            path.append((i, j))
            if grid[i][j] == 0:
                print("YES")
                formatted_path = " -> ".join(str(p) for p in path)
                print(f"{formatted_path} -> 0 도달 -> 성공")
                return 
    print("NO")

# 메인 함수
# 격자 크기 입력받아 격자 생성 및 출력
def main():
    size = int(input("격자 크기를 입력하세요 (예: 3): "))
    grid = generate_grid(size)

    print("\n생성된 격자:")
    print_grid(grid)

    print("\n경로 추적:")
    find_zero_with_path(grid)

if __name__ == "__main__":
    main()