import heapq

def find_min_limit():
    # 우선순위 큐에 (limit, cnt, dir, x, y)
    pq = []
    heapq.heappush(pq, (0, 0, 0, start[0], start[1]))

    # 방문한 상태만 기록하는 set
    visited = set()

    while pq:
        limit, cnt, dir, x, y = heapq.heappop(pq)
        state = (x, y, dir, cnt)

        # 이미 방문한 상태면 스킵
        if state in visited:
            continue
        visited.add(state)

        # 보석에 도달했다면 그 순간의 limit 반환
        if (x, y) == end:
            return limit

        # 공중 상태 (dir != 0)
        if dir != 0:
            nx, ny = x + dir, y
            if 0 <= nx < n:
                cell = grid[nx][ny]
                # 빈칸이면 공중 계속
                if cell == 0:
                    ncnt = cnt + 1
                    heapq.heappush(pq, (max(limit, ncnt), ncnt, dir, nx, ny))
                # 땅이나 보석이면 착지
                if cell in (1, 3):
                    ncnt = cnt + 1
                    heapq.heappush(pq, (max(limit, ncnt), 0, 0, nx, ny))

        # 지상 상태 (dir == 0)
        else:
            # 좌우 이동
            for dy in (-1, 1):
                nx, ny = x, y + dy
                if 0 <= ny < m and grid[nx][ny] in (1, 3):
                    heapq.heappush(pq, (limit, 0, 0, nx, ny))

            # 수직 이동 시작
            for dx in (-1, 1):
                nx, ny = x + dx, y
                if 0 <= nx < n:
                    cell = grid[nx][ny]
                    # 빈칸이면 공중 시작
                    if cell == 0:
                        heapq.heappush(pq, (max(limit, 1), 1, dx, nx, ny))
                    # 땅이나 보석이면 바로 착지
                    elif cell in (1, 3):
                        heapq.heappush(pq, (max(limit, 1), 0, 0, nx, ny))


# 입력 읽기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 시작과 보석 위치 찾기
start = end = None
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            start = (i, j)
        elif grid[i][j] == 3:
            end = (i, j)

print(find_min_limit())

# bfs로 돌면서 방향넣어서 limit 갱신
