import sys
sys.stdin = open("input.txt", "r")

def balloon_game(balloon_lst):
    # 남은 풍선이 한 개이면, 점수는 그 풍선의 숫자
    if len(balloon_lst) == 1:
        return balloon_lst[0]
    
    max_sum = float('-inf')
    for i in range(len(balloon_lst)):
        # 풍선의 위치에 따라 점수 계산
        if i == 0:  # 가장 왼쪽인 경우, 오른쪽 풍선만 이웃
            score = balloon_lst[1]
        elif i == len(balloon_lst) - 1:  # 가장 오른쪽인 경우, 왼쪽 풍선만 이웃
            score = balloon_lst[-2]
        else:
            # 양쪽 이웃이 존재하는 경우 두 이웃의 곱
            score = balloon_lst[i - 1] * balloon_lst[i + 1]
        # 해당 풍선을 터트린 후 남은 풍선들의 상태
        new_balloon_lst = balloon_lst[:i] + balloon_lst[i + 1:]
        max_sum = max(max_sum, score + balloon_game(new_balloon_lst))
        
    return max_sum

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    balloons = list(map(int, sys.stdin.readline().split()))
    
    result = balloon_game(balloons)
    print(f"#{t} {result}")

# 풍선 하나면 바로 저장 하나가 아니면 balloon 길이 만큼 돌면서 최댓 값 저장하고 
# 풍선 터뜨리고 text로 남은 풍선 balloon list에 저장하고 
# 그 balloon 텍스트 함수 재귀
