grid = [
    list("S...#....."),
    list("###.#.###."),
    list("........#."),
    list(".######.#."),
    list("......#.#."),
    list(".#.#..#.#."),
    list(".#.####.#."),
    list("........#."),
    list(".######.#."),
    list("........E.")
]

def move(maze, x, y, count=0):
    # 현재 위치가 도착 지점 'E'라면 종료
    if maze[y][x] == 'E':
        print(f"도착! 위치: ({x}, {y}), 이동 횟수: {count}")
        return True

    # 오른쪽으로 이동 가능한 경우 ('.' 또는 'E')이면 오른쪽 재귀 호출
    if x + 1 < 10 and maze[y][x + 1] in ['.', 'E']:
        if move(maze, x + 1, y, count + 1):  # x+1: 오른쪽, y: 같은 행
            return True

    # 아래쪽으로 이동 가능한 경우 ('.' 또는 'E')이면 아래쪽 재귀 호출
    if y + 1 < 10 and maze[y + 1][x] in ['.', 'E']:
        if move(maze, x, y + 1, count + 1):  # x: 같은 열, y+1: 아래쪽
            return True

    # 도달 불가능한 경우 False 반환 (백트래킹 없음, 단순 종료)
    return False

# 시작점 (0,0)에서 탐색 시작
move(grid, 0, 0)
