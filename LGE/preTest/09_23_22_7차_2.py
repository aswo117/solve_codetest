# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 최대 수업을 들을 수 있어야 되니, x0 기준이 아니라 x1 기준으로 정렬해야 한다.
# x1 로 정렬해야 될 때 lamda 의 활용법을 이해하자
# ex 1. sort(key=lamda x : (x[1], x[0])) --> x[1]로 정렬하고 같으면 x[0] 기준으로 정렬하는 방법
# ex 2. List의 Data는 그대로 두고 index 값만 바꾸는 방법이 있다.
#       index_list = list(range(len(a)))
#       index_list.sort(key = lamda x : a[x])
import sys
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int,readl().split())) for _ in range(N)]
    return N, info
 
ans = 1
N, info = Input_Data() # 입력 받는 부분
 
# print(N)
# print(info)
# 여기서 부터 작성

time_list = list()

for i in range(N):
	time_list.append((info[i][0], info[i][0] + info[i][1] + 2)) # End 시간은 처음시간 + 걸리는 시간 + 휴식시간(2시간)
# print(time_list)

time_list.sort(key=lambda x : (x[1]))

compare_time = time_list[0][1]
for i in range(1, N):
	if compare_time <= time_list[i][0]: # 들은 수업의 시작시간과 다음 수업의 끝시간비교 시 다음 수업이 같거나 크면 수업 들을 수 있음
		compare_time = time_list[i][1]    # 비교시간은(Start 시간) 들을 수 있는 수업의 끝시간
		ans = ans+1
		# print(f"compare_time = {compare_time}")
 
print(ans) # 출력 하는 부분
