# import sys
# sys.stdin = open("input.txt", "r")


def selling_honeycomb(current_max):
    global max_sum

    if len(path) == 4:
        if max_sum < current_max:
            
            max_sum = current_max
            # print(path)
        return

    lst = set()
    for temp in path:

        ty = temp[0]
        tx = temp[1]

        if tx % 2 == 1:
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, -1], [1, 1]]
        else:
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1]]

        for dy, dx in direction:
            ny, nx = ty + dy, tx + dx


            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in path:
                lst.add((ny, nx))

    temp_lst = []
 
 
    for q in lst:
        temp_lst.append(q) 
    # print(temp_lst)
    for temp in temp_lst:
        ny = temp[0]
        nx = temp[1]
        if visited[ny][nx] == 1: continue
        visited[ny][nx] = 1
        path.add((ny, nx))
        selling_honeycomb(current_max + arr[ny][nx])
        path.remove((ny, nx))
        visited[ny][nx] = 0


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_sum = float('-inf')
    visited = [[0]*m for _ in range(n)]
    

    
    for i in range(n):
        for j in range(m):
            path = set()
            start= set()

            path.add((i, j))
            visited[i][j] = 1
            selling_honeycomb(arr[i][j])
  

    print(f'#{tc} {max_sum}')

# 모든 좌표에서 돌리기
# direction 행이 짝수일 때와 홀수일 때 나누기
# set에 선택되어진 좌표들과 붙어있는 곳 모두 넣어서 다음 갈 곳 모두 저장
# 그 다음 붙어있는 좌표들을 dfs로 돌기