from copy import deepcopy


def spin_array(temp_arr, x, y, power):
    arr = deepcopy(temp_arr)
    for p in range(1, power + 1):
        for i in range(-p, p + 1):
            for j in range(-p, p + 1):
                # 테두리만 처리
                if not (i == -p or i == p or j == -p or j == p):
                    continue

                r0 = x - 1 + i
                c0 = y - 1 + j

                # 꼭짓점
                if i == -p and j == -p:
                    arr[r0][c0] = temp_arr[r0 + 1][c0]
                elif i == -p and j == p:
                    arr[r0][c0] = temp_arr[r0][c0 - 1]
                elif i == p and j == -p:
                    arr[r0][c0] = temp_arr[r0][c0 + 1]
                elif i == p and j == p:
                    arr[r0][c0] = temp_arr[r0 - 1][c0]
                else:
                    # 변 (꼭짓점 제외)
                    if i == -p:      # top edge
                        arr[r0][c0] = temp_arr[r0][c0 - 1]
                    elif i == p:     # bottom edge
                        arr[r0][c0] = temp_arr[r0][c0 + 1]
                    elif j == -p:    # left edge
                        arr[r0][c0] = temp_arr[r0 + 1][c0]
                    elif j == p:     # right edge
                        arr[r0][c0] = temp_arr[r0 - 1][c0]
    return arr

def find_min(arr):
    return min(sum(i) for i in arr)

def make_permutations(visited, current, result, k):
    if len(current) == k:
        result.append(current[:])
        return
    for i in range(k):
        if visited[i] == 0:
            visited[i] = 1
            current.append(i)
            make_permutations(visited, current, result, k)
            current.pop()
            visited[i] = 0

t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    ops = []
    for _ in range(k):
        r, c, s = map(int, input().split())
        ops.append((r, c, s))

    orders = []
    make_permutations([0] * k, [], orders, k)

    res = float('inf')
    for order in orders:
        temp = deepcopy(arr)
        for idx in order:
            x, y, p = ops[idx]
            temp = spin_array(temp, x, y, p)
        res = min(res, find_min(temp))

    print(f'#{tc} {res}')


# 순서가 안정해져 있으니깐 일단 순열을 구하고
# 순열 대로 배열 돌리기
# 모서리 하고 변 돌리기기