import random

# grid 생성 함수
def generate_grid(size):
    grid = []
    for i in range(size):
        row = []
        for i in range(size): # 열에 대한 list 생성
            row.append(random.randint(1, size-1)) # 각 셀의 숫자는 0부터 size-1까지의 랜덤 숫자
        grid.append(row)
    
    zero_x = random.randint(0, size-1)
    zero_y = random.randint(0, size-1)
    grid[zero_x][zero_y] = 0
    return grid

# Matrix 출력 함수
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# DFS 함수 정의의
def dfs(grid, x, y, visited, path):
    size = len(grid) # grid의 크기 행 개수로 정의
    # 경계 조건: x, y가 grid의 범위를 벗어나거나 이미 방문한 경우
    if x < 0 or x >= size or y < 0 or y >= size or visited[x][y]:
        return False
    
    # 경로 좌표를 path에 저장 후 True로 지정
    path.append((x, y))
    visited[x][y] = True

    # 0을 만났을 때
    if grid[x][y] == 0:
        print("YES") # 0 도달 여부 출력
        print(" -> ".join(f"{p}={grid[p[0]][p[1]]}" for p in path) + " -> 0 도달 -> 성공") # 도달 경로 출력
        print(f'최소값 이동한 셀: {", ".join(f"{p}={grid[p[0]][p[1]]}" for p in path)}') # 최솟값으로 이동한 셀 출력
        print(f'총합: {sum(grid[p[0]][p[1]] for p in path)}') # 경로의 총합 출력
        return True

    # 몇 칸을 어디로 옮길 것인지 결정
    step = grid[x][y] # 현재 셀 숫자가 이동할 칸 수
    directions = [(-step, 0), (step, 0), (0, -step), (0, step)]  # 상, 하, 좌, 우

    candidates = [] # 후보 리스트 (상, 하, 좌, 우)
    # 움직일 셀 좌표를 candidates에 저장
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # 후보 좌표가 grid의 범위 내에 있고, 방문하지 않은 경우 후보로 등록
        if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny]:
            candidates.append(((dx, dy), grid[nx][ny]))

        # 값 기준으로 정렬 (작은 값 우선)
    candidates.sort(key=lambda item: item[1])

    # 후보 좌표로 이동
    for (dx, dy), _ in candidates:
        nx, ny = x + dx, y + dy
        if dfs(grid, nx, ny, visited, path): # 한 번 움직였을 때 0에 도착하지 않았다면 함수 다시 호출
            return True
        
        # 이동한 좌표가 0이 아니면 경로에서 제거
        path.pop() # 이번 경로에서 마지막 셀 제거
        visited[x][y] = False # 다른 경로에서 이 셀을 갈 수 있도록 방문기록 초기화
        return False

grid = [
    [3, 4, 1, 2, 5, 2, 3, 2, 1, 1],
    [1, 2, 3, 2, 1, 4, 2, 2, 3, 2],
    [2, 1, 1, 3, 2, 1, 1, 3, 1, 2],
    [3, 2, 4, 2, 3, 1, 2, 1, 4, 2],
    [1, 3, 2, 1, 1, 2, 4, 3, 2, 3],
    [2, 2, 1, 4, 3, 3, 1, 2, 3, 1],
    [1, 1, 2, 1, 2, 4, 3, 1, 2, 1],
    [3, 3, 1, 2, 3, 1, 1, 4, 2, 2],
    [2, 1, 2, 3, 2, 2, 1, 2, 3, 1],
    [1, 2, 1, 1, 1, 1, 1, 3, 2, 0]  # (9, 9)이 도착점
]



# 실행 함수
def run_escape_algorithm(size):
    print("\n경로 추적:")
    visited = [[False]*size for i in range(size)] # 방문 여부 저장
    if not dfs(grid, 0, 0, visited, []):
        print("NO")

# 예시 실행
run_escape_algorithm(10)

# 최종 결과 도합 26