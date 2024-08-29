#https://www.acmicpc.net/problem/2110
#total 의 조건이 == C 일때만 찾으면 안됨 (12%Err)
#>= C 조건도 가능한데, 중간에 하나 빼도 몰 루 이기 때문.. ? 맞나 

import sys
from collections import deque
import math

input = sys.stdin.readline

#print(f"[+][sung]")

N, C = map(int, input().split())
data_list = list()

for i in range(N):
	data_list.append(int(input()))

data_list.sort()
# print(data_list)

def check(m):
	count = 1 #공유기 개수
	# dist_m = 0
	start_point = 0
	
	# print("check start")
	# print(f"[+][sung] m = {m}")
	
	for idx, i in enumerate(data_list):
		# print(f"[+][sung] {m} - ({data_list[idx]} - {data_list[start_point]}) = {m - (data_list[idx] - data_list[start_point])} ")
		if m - (data_list[idx] - data_list[start_point]) <= 0:	#공유기 사이의 거리가 집사이의 거리보다 작으면
			# print("[+][sung] count ++")
			count = count+1
			start_point = idx
	# print(f"[+][sung] count = {count}")
	return count

S = 1
E = 1000000000
max_mid = 0

while S<=E:	
	mid = (S+E)//2		#공유기 사이의 거리
	total = check(mid)
	
	if total == 0:		#total : 설치된 공유기의 개수
		# print(f"[+][sung] total = 0")
		E = mid
		continue
	elif total >= C:	#설치 해야하는 공유기 개수보다 믾이 설치했으므로		
		S = mid+1
		if max_mid <= mid:
			max_mid = mid			
	else:
		E = mid-1
	
print(max_mid)
