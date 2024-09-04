# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
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

time_list.sort()

compare_time = time_list[0][1]
for i in range(1, N):
	if compare_time <= time_list[i][0]: # 들은 수업의 시작시간과 다음 수업의 끝시간비교 시 다음 수업이 같거나 크면 수업 들을 수 있음
		compare_time = time_list[i][1]    # 비교시간은(Start 시간) 들을 수 있는 수업의 끝시간
		ans = ans+1
		# print(f"compare_time = {compare_time}")
 
print(ans) # 출력 하는 부분
