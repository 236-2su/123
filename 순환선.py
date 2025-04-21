# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1,T+1):
    N= int(input())
    arr = list(map(int,input().split()))
    result = 0
    validity =float('-inf')
    for a in range(N-4):
        for b in range(a+2 ,N-2):
            for c in range(b+2,N):
                for d in range(N):
                    if d>= c+2 or a-2>=d:
                        if b-a ==1 or c-b ==1 or d-c ==1 or a-d ==1 or d-a ==N-1 or c-d==N-1:
                            continue
                        else:
                            result = (arr[a]+arr[b])**2+(arr[c]+arr[d])**2
                            if result> validity:
                                validity = result
    print(f'#{t} {validity}')


# 4중 for문 돌려서 하나하나 정하고 나머지 정하기
# 원이기 때문에 abcd 자리바꾼 거는 똑같은 거
# tip d가 0으로 넘어왔을 때 c가 n-1일 때 e 두가지 경우 생각하면됨.
