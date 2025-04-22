def dfs(x, y, path):
    if not (0 <= x < n and 0 <= y < n):  # 범위 체크
        return False
    if visited[x][y]:
        return False

    path.append((x, y))  # 현재 위치 추가
    visited[x][y] = True
    jump = grid[x][y]

    if jump == 0:
        print("YES")
        print(" → ".join(str(p) for p in path), "→ 0 도달 → 성공")
        return True

    # 상하좌우 이동
    for dx, dy in [(-jump,0), (jump,0), (0,-jump), (0,jump)]:
        if dfs(x + dx, y + dy, path.copy()):  # 복사된 경로로 이어감
            return True

    return False

# 입력
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

# 실행
if not dfs(0, 0, []):
    print("NO")