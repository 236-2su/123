# import sys
# sys.stdin = open("input.txt", "r")
import copy


def meeting_last_apple(N,M,last_number,arr):
    jnudge_number = 0
    count = 0
    location = [0,0]
	  # 마지막 번호 전까지 돌기 만나면 끝이니깐   
    while jnudge_number < last_number:
		    # 한개를 찾고 다음 돌 때는 다음 번호를 입력
        check_number =jnudge_number+1
        # 4로 나눠서 4방향으로 갈거기 때문에 4를 나눈 나머지 입력
        percent_=count%4
        # matching에 체크해야할 다음 좌표 저장
        matching= M[check_number] 
        if percent_ == 0:
            # 0 이면 오른쪽으로 한칸씩 감
            location[1] += 1
            # 만약 가는데 벽에 부딫히기 전에 우회전하면 만나게 되면 그 x값으로 갔을 떄 우회전
            if location[1] == matching[1] and location[0] < matching[0]:

                count += 1 
                jnudge_number += 1 
                location = copy.deepcopy(matching)
                continue
            # 위에 if에 해당안하고 벽 만나면 우회전
            elif location[1]==N-1:
                count +=1
                continue
				# 오른쪽으로가다 우회전하면 아래로 감                    
        elif percent_ == 1:
            location[0] += 1
            # 내려가다 오른쪽에 있으면 벽에 닿기 전에 우회전
            if location[0] == matching[0] and location[1] > matching[1]:
                count += 1
                jnudge_number += 1
                location = copy.deepcopy(matching)
                continue
            # 아니면 벽까지감
            elif location[0] == N-1:
                count +=1
                continue
	       # 아래로 내려가다 우회전하게 되면 왼쪽으로감
        elif percent_ == 2:
            location[1] -= 1
            # 가다가 벽에 닿기 전에 우회전해서 만날 수 있으면 우회전
            if location[1] == matching[1] and location[0] > matching[0]:
                count += 1
                jnudge_number += 1
                location = copy.deepcopy(matching)
                continue
            # 아니면 벽에 가서 우회전
            elif location[1]==0:
                count +=1
                continue
        # 왼쪽으로 가다가 우회전하면 위로감      
        elif percent_ == 3:
            location[0] -= 1
            
	          # 가다가 우회전해서 만날 수 있으면 우회전
            if location[0] == matching[0] and location[1] < matching[1]:
                count += 1
                jnudge_number += 1
                location = copy.deepcopy(matching)
                continue
	          # 못만나면 벽에가서 우회전
            elif location[0]==0:
                count +=1     
                continue
    return count

T = int(input())
for t in range(1,T+1):
    N= int(input())
    arr = [list(map(int,input().split())) for i in range(N)]
    M=[0]*11
    last_number =0
    for i in range(N):
        for j in range(N):
		        # 돌면서 사과 숫자를 index에 맞게 입력
            if arr[i][j] != 0:
                M[arr[i][j]] = [i,j]
                # 언제까지 돌지 알려면 마지막 숫자를 알아야함
                if last_number < arr[i][j]:
                    last_number =arr[i][j]

    
    print(f'#{t} {meeting_last_apple(N,M,last_number,arr):}')

    # 사과를 dat배열에 차례대로 저장하고 방향을 4로 나눈 나머지로 방향을 정한다
    # 가는 길에 오른쪽에 있으면 오른쪽으로 돌고 다음 사과 찾기
    # 벽까지가면 오른쪽으로 돌아서 경로 정하기