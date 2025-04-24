grid = [
    list("S...#....."),
    list("###.#.###."),
    list("........#."),
    list(".######.#."),
    list("......#.#."),
    list(".#.#..#.#."),
    list(".#.####.#."),
    list("……..#."),
    list(".######.#."),
    list("……..E.")
]

def move(maze, x, y, count=0):
    # 종료 조건: E를 만나면 탐색 종료
    if maze[y][x] == 'E':
        print(f"도착! 위치: ({x}, {y}), 이동 횟수: {count}")
        return True

    # 오른쪽으로 이동 가능하면
    if x + 1 < 10 and maze[y][x + 1] in ['.', 'E']:
        if move(maze, x + 1, y, count + 1):
            return True

    # 아래로 이동 가능하면
    if y + 1 < 10 and maze[y + 1][x] in ['.', 'E']:
        if move(maze, x, y + 1, count + 1):
            return True

    return False  # 도달 불가능하면 false 반환
move(grid,0,0)