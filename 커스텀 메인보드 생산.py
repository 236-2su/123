# import sys
# sys.stdin = open("input.txt", "r")
from collections import deque



# 부품 그룹화 BFS로 같은 부품끼리 묶기
def label_components():
    # 부품 번호는 2부터 시작 (1은 원래 부품)
    label = 2 
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                queue = deque([(i, j)])
                arr[i][j] = label
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                            arr[nx][ny] = label
                            queue.append((nx, ny))
                label += 1
    # 총 부품 수 반환
    return label - 2  

# 케이블 연결 가능한 후보 찾기
def find_edges():
    edges = []
    for i in range(n):
        for j in range(m):
             # 부품이라면
            if arr[i][j] >= 2: 
                start = arr[i][j]
                for dx, dy in directions:
                    length = 0
                    x, y = i, j
                    while True:
                        x += dx
                        y += dy
                        if not (0 <= x < n and 0 <= y < m): break
                        # 같은 부품이면 중단
                        if arr[x][y] == start: break  
                        if arr[x][y] == 0:
                            # 빈 칸이면 길이 증가
                            length += 1  
                        else:
                             # 길이 2 이상일 때만 유효
                            if length >= 2: 
                                end = arr[x][y]
                                edges.append((length, start, end))
                            break
    return edges

# 유니온-파인드 (find)
def find_set(x):
    if boss[x] == 0:
        return x
    result = find_set(boss[x])
    boss[x] = result  
    return result

# 유니온-파인드 (union)
def union(t1, t2):
    a = find_set(t1)
    b = find_set(t2)
    if a == b:
        return
    boss[b] = a  

# 메인 문제 풀이
def solve_arr_problem():
    global boss
    num_components = label_components()  
    edges = find_edges() 
	# 유니온파인드 부모 테이블 초기화
    boss = [0] * (2 + num_components + 2)  
	
    # 거리 짧은 순으로 정렬
    edges.sort()  
    total = 0
    count = 0

    for cost, a, b in edges:
        if find_set(a) != find_set(b):
            union(a, b)
            total += cost
            count += 1
            if count == num_components - 1:
                break
    root_set = set() 

    for i in range(2, 2 + num_components): 
        root = find_set(i)  
        root_set.add(root)  

    if len(root_set) == 1:
        return total
    else:
        return -1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

result = solve_arr_problem()
print(result)


# 붙어있는 부품들을 같은 숫자로 만듦
# length ,start, end 해서 부품들간의 간선을 만들고 가중치를 추가함
# 가중치가 작은 것부터 넣기 위해 sort를해서 오름차순 정렬 후, union-find 실행

