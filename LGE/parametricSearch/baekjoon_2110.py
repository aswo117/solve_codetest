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
	elif total > C:	#설치 해야하는 공유기 개수보다 믾이 설치했으므로
		# print(f"[+][sung] total > C")
		S = mid+1
	elif total == C:	#설치해야 하는 공유기 개수인 C 
		# print(f"[+][sung] total == C")
		if max_mid <= mid:
			max_mid = mid
		break
	else:
		E = mid-1
	
print(max_mid)
