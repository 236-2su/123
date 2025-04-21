import heapq
# import sys
#sys.stdin = open("input.txt", "r")

def find_route():
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]  

    while pq:
        fuel, x, y = heapq.heappop(pq)
        if dist[x][y] < fuel:
            continue

        
        for dy, dx in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= ny < n and 0 <= nx < n:
                diff = arr[nx][ny] - arr[x][y]
                if diff < 0:
                    cost = 0
                elif diff == 0:
                    cost = 1
                else:
                    cost = diff * 2

                if dist[nx][ny] > fuel + cost:
                    dist[nx][ny] = fuel + cost
                    heapq.heappush(pq, (fuel + cost, nx, ny))

        
        for t in tunnel:
            (x1, y1), (x2, y2), w = t
            if (x, y) == (x1, y1):
                if dist[x2][y2] > fuel + w:
                    dist[x2][y2] = fuel + w
                    heapq.heappush(pq, (fuel + w, x2, y2))
            elif (x, y) == (x2, y2):
                if dist[x1][y1] > fuel + w:
                    dist[x1][y1] = fuel + w
                    heapq.heappush(pq, (fuel + w, x1, y1))

    return dist[n-1][n-1]


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    tunnel = []

    for _ in range(m):
        x1, y1, x2, y2, w = map(int, input().split())
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        tunnel.append([(x1, y1), (x2, y2), w])

    result = find_route()
    print(f'#{tc} {result}')

# 다익스트라 + 터널 계산