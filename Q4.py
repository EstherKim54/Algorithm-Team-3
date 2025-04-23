import random

# gid 생성 함수
# matrix를 list 구조로 반환
def generate_grid(size):
    grid = []
    for i in range(size):
        row = []
        for i in range(size): # 열에 대한 list 생성
            row.append(random.randint(0, size - 1))  # 최대 size-1까지만 생성
        grid.append(row)
    return grid

# Matrix 출력 함수
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# DFS 함수
def dfs(grid, x, y, visited, path):
    size = len(grid)
    if x < 0 or x >= size or y < 0 or y >= size or visited[x][y]:
        return False
    
    # 경로 좌표를 path에 저장 후 True로 지정
    path.append((x, y))
    visited[x][y] = True

    # 0을 만났을 때
    if grid[x][y] == 0:
        print("YES")
        print(" -> ".join(str(p) for p in path) + " -> 0 도달 -> 성공")
        return True

    # 몇 칸을 어디로 옮길 것인지 결정
    step = grid[x][y]
    directions = [(-step, 0), (step, 0), (0, -step), (0, step)]  # 상, 하, 좌, 우

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if dfs(grid, nx, ny, visited, path): # 새롭게 도달한 좌표로 다시 한 번 dfs 함수 동작
            return True

    path.pop()
    visited[x][y] = False
    return False

# 실행 함수
def run_escape_algorithm(size):
    grid = generate_grid(size)
    print_grid(grid)
    print("\n경로 추적:")
    visited = [[False]*size for i in range(size)]
    if not dfs(grid, 0, 0, visited, []):
        print("NO")

# 예시 실행
run_escape_algorithm(4)