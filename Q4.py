import random

# gid 생성 함수
# matrix를 list 구조로 반환
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
        print(" -> ".join(f"{p}={grid[p[0]][p[1]]}" for p in path) + " -> 0 도달 -> 성공")
        print(f'최소값 이동한 셀: {", ".join(f"{p}={grid[p[0]][p[1]]}" for p in path)}')
        print(f'총합: {sum(grid[p[0]][p[1]] for p in path)}')
        return True

    # 몇 칸을 어디로 옮길 것인지 결정
    step = grid[x][y]
    directions = [(-step, 0), (step, 0), (0, -step), (0, step)]  # 상, 하, 좌, 우

    candidates = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and not visited[nx][ny]:
            candidates.append(((dx, dy), grid[nx][ny]))

        # 값 기준으로 정렬 (작은 값 우선)
    candidates.sort(key=lambda item: item[1])

    for (dx, dy), _ in candidates:
        nx, ny = x + dx, y + dy
        if dfs(grid, nx, ny, visited, path):
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
run_escape_algorithm(int(input("격자 크기: ")))