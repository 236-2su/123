
import copy

def dfs(depth, r, c, captured):
    # 그좌표 그위치에 잡혀진 쫄의 좌표들이 같으면 다시 볼 필요 없음 가지치기
    #  tuple에 sorted를 한 이유는 지나왔던 위치가 달라서 같은 좌표들이 들었어도 순서가 다르게 저장되어 있으면 확인을 못함
    state = (depth, r, c, tuple(sorted(captured)))
    if state in visited:
        return
    visited.add(state)
    # 포는 최대 3번 이동할 수 있음
    if depth == 3:
        return

    for dr, dc in directions:
        found_jump = False
        step = 1
        while True:
            nr = r + dr * step
            nc = c + dc * step
            # 범위 벗어나면 중단
            if not (0 <= nr < n and 0 <= nc < n):
                break

            pos = (nr, nc)
            if not found_jump:
                # 아직 뛰어넘을 쫄을 찾지 않은 상태
                if pos in initial_soldiers:
                    # 뛰어넘을 쫄을 찾았고 이전에 확인을 안한 상태이면
                    found_jump = True
                step += 1
                continue
            else:
                # 뛰어넘은 후, 갈 수 있는 경로 탐색
                if pos in initial_soldiers and pos not in captured:
                    # 뛰어 넘은 이후 쫄을 만나면 거기서 잡고 잡았다고 표시하는 set에 집어넣음
                    new_captured = copy.deepcopy(captured)  
                    new_captured.add(pos)          
                    global_captures.add(pos)
                    dfs(depth + 1, nr, nc, new_captured)
                    # 잡은 다음, 해당 방향의 탐색 중단
                    break
                else:
                    # 쫄을 만난게 아니라면 그자리에서도 한번 더 재귀 실행
                    dfs(depth + 1, nr, nc, captured)
                    step += 1

t = int(input())

# 상, 하, 좌, 우 이동 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, t + 1):
    n = int(input())
    board = []
    cannon_pos = None
    initial_soldiers = set()
    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        
        for j in range(len(row)):
            val = row[j] 
            # 포위치 입력
            if val == 2:
                cannon_pos = (i, j)
            elif val == 1:
                # 쫄들 위치 저장
                initial_soldiers.add((i, j))
    
    global_captures = set()
    visited = set()
    
    dfs(0, cannon_pos[0], cannon_pos[1], set())
    
    print(f"#{tc} {len(global_captures)}")


# 일단 포위치랑 쫄들 위치를 따로 저장
# (depth,포 x,포y, 잡은쫄들위치 집합) 으로 dfs 돌리기
# 방문한 곳을 visited 집합에 넣기
# depth가 3이면 문제에서 최대 3번까지 이동가능하다고 되어 있음
# 움직이려면 일단 넘어야하는 쫄들을 찾아야함
# 넘어야하는 쫄을 못 찾고 벽까지 가면 끝
# 초기 쫄들의 위치 저장한 곳에 도착하면 점프가능하다고 flag수정
# 만약 flag처리해서 이미 점프를 하고 쫄을 만났으면 
# new_captured는 captured를 deepcopy하고 global_captures에 추가하고 재귀다시 돌기
# 한번 넘은 자리에서 또 넘을 곳을 찾아야 하니깐 그자리에서 잡은게 아니라면 재귀 실행