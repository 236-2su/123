# import sys
# sys.stdin = open("input.txt", "r")

def find_size(i, j):
    for s in range(5, 0, -1):
        flag = 0
        for x in range(s):
            for y in range(s):
                if 0 <= i+x < 10 and 0 <= j+y < 10:
                    if arr[i+x][j+y] != 1:
                        flag = 1
                        break
                else:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            size_with_location[i][j].append(s)
    return

def can_place(i, j, s):
    if i + s > 10 or j + s > 10:
        return 0
    for x in range(s):
        for y in range(s):
            if arr[i+x][j+y] != 1:
                return 0
    return 1

def dfs(count):
    global ans
    
    if count >= ans:
        return

    found = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                found = 1
                start_i, start_j = i, j
                break
        if found:
            break

    if not found:
        ans = min(ans, count)
        return

    if size_with_location[start_i][start_j]:
        for s in size_with_location[start_i][start_j]:
            if papers[s] > 0 and can_place(start_i, start_j, s):

                for x in range(s):
                    for y in range(s):
                        arr[i+x][j+y] = 9  
                papers[s] -= 1
                
                dfs(count + 1)

                for x in range(s):
                    for y in range(s):
                        arr[i+x][j+y] = 1  
                papers[s] += 1
    else:
       
        return


t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(10)]
    papers = [0, 5, 5, 5, 5, 5]  
    ans = float('inf')
    
    size_with_location = [[[] for _ in range(10)] for _ in range(10)]
    
    
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                find_size(i, j)
    
        
    dfs(0)
    if ans != float('inf'):
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} -1')

# point는 papers [0,5,5,5,5,5] 로 최대 5개인거 
# 빈 2차원 배열을 만들어서 해당 좌표에 붙일 수 있는 색종이 크기 모두 저장
# dfs를 돌면서 만든 색종이 사이즈 만큼 다른 숫자로 바꿨다가 다시 백트래킹 해주기