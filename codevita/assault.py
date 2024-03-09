def mark(xa, ya, ha, matrix, visited):
    rows, cols = len(matrix), len(matrix[0])
    visited[xa][ya] = 1
    delta = [-1, 0, +1, 0, -1]
    for i in range(4):
        ax, ay = xa + delta[i], ya + delta[i + 1]
        if 0 <= min(ax, ay) < rows and ax < rows and ay < cols and matrix[ax][ay] <= ha and not visited[ax][ay]:
            mark(ax, ay, ha, matrix, visited)


def go2(x, y, cell, matrix, visited):
    rows, cols = len(matrix), len(matrix[0])
    delta = [-1, 0, +1, 0, -1]
    visited[x][y] = 0
    for i in range(4):
        nx, ny = x + delta[i], y + delta[i + 1]
        if 0 <= min(nx, ny) < rows and nx < rows and ny < cols and matrix[nx][ny] == cell and visited[nx][ny]:
            go2(nx, ny, cell, matrix, visited)


def main():
    rows, cols = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    visited = [[0] * cols for _ in range(rows)]

    x, y = map(int, input().split())
    h = int(input())

    if matrix[x][y] == 0:
        mark(x, y, h, matrix, visited)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if visited[i][j]:
                count += matrix[i][j] != 0
                go2(i, j, matrix[i][j], matrix, visited)

    if count == 0:
        print("NONE")
    else:
        print(count)


if __name__ == "__main__":
    main()
