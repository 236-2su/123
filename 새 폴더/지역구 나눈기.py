#import sys
# sys.stdin = open("input.txt","r")

# 연결되어 있는지 확인 하는 함수
def is_connected(linked_lst, excluded_nodes):
		# 지정해 놓은 노드가 아닌 노드들에 없으면 
    if not excluded_nodes:
        return False 
    
    # visited 배열 초기화
    visited = set()
    # 그냥 아무 노드나 넣어도 됨, 모두 연결 되어 있는지 확인해야 하니깐
    temp_arr = [excluded_nodes[0]]  
    
    # 하나씩 빼서 다른 노드랑 연결 되어 있는지 확인
    while temp_arr:
		    # 하나 빼서 연결되어 있는지 확인 bfs처럼 했음
        node = temp_arr.pop()
        
        if node in visited:
            continue
	       # 연결되어 있는 노드 모두 추가
        visited.add(node)
        # 빼서 확인하는 노드에 연결되어 있는 노드들 모두 확인
        for z in linked_lst[node]:
            if z in excluded_nodes and z not in visited:
                temp_arr.append(z)
    # set로 되어 있기 때문에 길이가 같으면 모두 연결 되어 있는 거임
    return len(visited) == len(excluded_nodes)  


def find_case(lev, i):
    global min_differ
    temp = []
		
	# 전역탐색하면서 가질 수 있는 모든 부분집합 중 해당 안되는 노드들 모두 temp에 저장    
    for k in range(1, n + 1):
        if k not in path:
            temp.append(k)

	# 제외한 노드들이 연결되어 있는지 돌림
    if is_connected(lst, temp):  
        a, b = 0, 0 
        # 반으로 나뉜 노드 들을 따로 나눠서 합함
        for o in path:
            a += int(value[o - 1]) 
        for o in temp:
            b += int(value[o - 1])
        # 차이의 최솟값을 저장
        min_differ = min(abs(a - b), min_differ)
    # 경우의 수가 n개의 길이 이상일 수 없기 때문
    if lev == n:  
        return
    # 갈 수 있는 노드들을 하나씩 저장
    for j in lst[i]:
        if not visited[j]:
            path.append(j)
            visited[j] = 1
            find_case(lev + 1, j)
            path.pop()
            visited[j] = 0  

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    value = list(map(int, input().split()))
    
    lst = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    path = []
    # 연결 되어 있는 곳 index에 맞게 모두 lst에 넣기
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                lst[i + 1].append(j + 1)

    min_differ = float('inf')
    
    # 노드어디를 기준으로 해야 하는지 모르기 때문에 모두 돌면서 해결
    for i in range(1, n + 1):
        visited[i] = 1
        path.append(i)
        find_case(0, i)
        path.pop()
        visited[i] = 0

    print(f'#{tc} {min_differ}')

    # 연결되어 있는 마을을 dat배열에 집어 넣기.
    # 어느 노드가 첫번째 노드인지 모르기 때문에 모든 node돌리기기
    # 부분 집합으로 연결된 마을 집어 넣고, path에 없는 마을들 따로 저장해서 
    # 서로 연결되어 있는지 확인하는 함수 돌리고 다 연결 되어 있으면 합구하기기
    # 연결되어 있는지 확인하는 함수는 bfs로 확인