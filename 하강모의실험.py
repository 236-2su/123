# import sys
# sys.stdin =open("input.txt","r")
def drop_simulator():
    col = list(arr[i])
    # 떨어지는 블록 인덱스 집합 
    removed = {0}
    # 초기 클러스터 크기: 맨 밑 블록 하나
    cluster_size = 1
    # 초기 낙하 에너지
    falling_force = 1.0
    # 현재 클러스터 바닥 인덱스
    bottom = 0

    while True:
        # 다음 블록 위치 찾기 (클러스터 바닥 위쪽)
        next_pos = None
        for j in range(bottom + 1, n):
            if col[j] == 1 and j not in removed:
                next_pos = j
                break
        # 더 이상 위에 블록이 없으면 최종 위치 계산 후 종료
        if next_pos is None:
            final_top = n - cluster_size
            break

        # 블록 사이 간격만큼 에너지 소모 및 바닥 위치 이동
        drop_d = next_pos - bottom - 1
        if drop_d > 0:
            falling_force *= (1.9 ** drop_d)
            bottom += drop_d

        # 다음 블록 클러스터 길이 세기
        start = next_pos
        cnt = 0
        for j in range(start, n):
            if col[j] == 1:
                cnt += 1
            else:
                break

        # 에너지가 충분하면 블록 흡수 후 클러스터 확장
        if falling_force > cnt:
            falling_force += cnt
            cluster_size += cnt
            for j in range(start, start + cnt):
                removed.add(j)
            bottom = start + cnt - 1
        # 에너지 부족하면 최종 클러스터 위치 결정 후 종료
        else:
            final_top = bottom - (cluster_size - 1)
            break

    # 제거된 블록 지우기
    for j in removed:
        col[j] = 0
    # 최종 위치에 클러스터 다시 그리기
    for j in range(final_top, final_top + cluster_size):
        col[j] = 1

    # 원래 배열에 반영
    arr[i] = col


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    # 입력 격자
    grid = [list(map(int, input().split())) for _ in range(n)]

    # 1) 세로 방향 시뮬레이션: 열 단위로 전환
    arr = [list(col) for col in zip(*grid)]
    for i in range(n):
        if arr[i][0] == 1:
            drop_simulator()
    # 다시 원래 격자로 복원
    grid = [list(row) for row in zip(*arr)]

    # 2) 가로 방향 시뮬레이션: 행 단위로 처리
    arr = [list(row) for row in grid]
    for i in range(n):
        if arr[i][0] == 1:
            drop_simulator()
    grid = arr

    # 결과: 맨 아래 행과 맨 오른쪽 열의 블록 개수 계산
    bottom_count = sum(grid[n-1])
    right_count  = sum(grid[r][n-1] for r in range(n))

    print(f"#{tc} {bottom_count} {right_count}")

# 행열을 바꿔서 일단 한번 열기준으로 아래로 내림 
# while문으로 pointer를 사용해서 bottom -> 움직이는 덩어리 가장아래를 기준으로 함
# removed를 만들어서 움직이는 박스들을 가져와서 나중에 다시 배열 재정의 해줌
