# import sys
# sys.stdin = open("input.txt", "r")

def solve_pipe_problem():
    count = 0  
    path = [(0, 1, 0)]  

    while path:
        x, y, direction = path.pop()

        if x == n - 1 and y == n - 1:
            count += 1
            continue

        if direction == 0 or direction == 2:
            ny = y + 1
            if ny < n and arr[x][ny] == 0:
                path.append((x, ny, 0))

        if direction == 1 or direction == 2:
            nx = x + 1
            if nx < n and arr[nx][y] == 0:
                path.append((nx, y, 1))

        nx, ny = x + 1, y + 1
        if nx < n and ny < n:
            if arr[x][ny] == 0 and arr[nx][y] == 0 and arr[nx][ny] == 0:
                path.append((nx, ny, 2))

    return count



t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = solve_pipe_problem()
    print(f"#{tc} {result}")
