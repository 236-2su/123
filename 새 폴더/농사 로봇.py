import copy


def count_harvest(start_x, start_y, dir):
    day = 0
    harvest_count = 0
    temp_arr = copy.deepcopy(arr)
    x, y = start_x, start_y
    # 각 위치에 씨가 심어진 횟수를 기록
    sprout_count = [[0]*n for _ in range(n)]

    while day < m:

        # 오전 빈농지이고 로봇이 다음 농지로 이동할 수 있는 경우 씨
        # 현재 빈농지이고 이동 못하면 가만히
        # 현재 농지에 곡식이 열린 경우 수확
        harvest = 0
        if temp_arr[x][y] >= 4+sprout_count[x][y]:
            # 추수하고
            harvest_count += 1
            # 빈농지 만들고
            temp_arr[x][y] = 0
            # 추수했다는 flag 추수했으면 씨를 심지 않으니깐
            harvest = 1

        # 이동 가능한 곳이 있는지 확인
        for nd in [(dir - 1) % 4, dir, (dir + 1) % 4, (dir + 2) % 4]:
            nx, ny = x + directions[nd][0], y + directions[nd][1]
            # 다음 가는 곳이 빈농지이거나 수확 가능한 곳이고 , 산이 아니라면
            if 0 <= nx < n and 0 <= ny < n and temp_arr[nx][ny] != 99 and (temp_arr[nx][ny] == 0 or temp_arr[nx][ny] >= 4+sprout_count[nx][ny]):

                # 빈농지고, 추수를 하지 않았으면 씨심기
                if temp_arr[x][y] == 0 and harvest == 0:
                    # 씨심기 => 하루지나면 1을 더해야하는데 1을 넣으면 안되니깐
                    temp_arr[x][y] = 0.5
                    # k 늘리고
                    sprout_count[x][y] += 1
                # 오후 이동
                x, y = nx, ny
                dir = nd
                break
        # 갈곳이 없으면 x,y 는 그대로 dir? 어느 방향?

        # 하루 경과: 모든 농지의 상태 업데이트
        for a in range(n):
            for b in range(n):
                # 씨가 심어진 농지라면, 산이 아니라면
                if temp_arr[a][b] > 0 and temp_arr[a][b] != 99:
                    # 곡식 익은 정도 증가
                    temp_arr[a][b] += 1

        day += 1

    return harvest_count


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_harvest = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # 산은 99로 표시
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                arr[i][j] = 99

    for i in range(n):
        for j in range(n):
            # 농지에서만 시작
            if arr[i][j] == 0:

                for d in range(4):
                    result = count_harvest(i, j, d)
                    max_harvest = max(result, max_harvest)

    print(f'#{tc} {max_harvest}')
