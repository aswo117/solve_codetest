#5% fail

import sys
from collections import deque
import math

input = sys.stdin.readline

#print(f"[+][sung] ")

#N 자르는 횟수가 담긴 목록
#M 자를 수 잇는 지점의 개수
#L 롤 케이크의 길이
N, M, L = map(int, input().split())
cutpoint_list = list()
cutcount_list = list()
result_list = list()

cutpoint_list.sort()
cutcount_list.sort()

cutpoint_list.append(int(0))
for i in range(M):
	cutpoint_list.append(int(input()))
for i in range(N):
	cutcount_list.append(int(input()))
	
# print(cutpoint_list)
# print(cutcount_list)

S = 1
E = 4000000 #L 이어도 되지 않을까?
max_mid = 0

#은 자르는 길이
def check(m):
	temp = 0
	start_point = 0
	new_cake_list = cutpoint_list + [L] #마지막 지점을 추가해줘야됨.
	for idx, data in enumerate(new_cake_list):
		# print(f"[+][sung] {m} - ({cutpoint_list[idx]}-{cutpoint_list[start_point]}) = {m - (cutpoint_list[idx]-cutpoint_list[start_point])}")
		if m - (new_cake_list[idx]-new_cake_list[start_point]) <= 0:
			temp = temp+1
			start_point = idx
	return temp	
	
#자르는 횟수(N, cutcount_list) 만큼 반복해야됨.
for i in cutcount_list:
	# print(f"i = {i}")
	while S<=E:
		mid = (S+E)//2
		total = check(mid)
		# print(f"[+][sung] mid = {mid}, total = {total}, cutpoint_list[-1] = {cutpoint_list[-1]}")
		#자르는 지점 중 가장 큰 지점보다 크면 pass
		# if total < cutpoint_list[-1]:
		# 	print("[+][sung] pass")
		# 	E = mid
		# 	continue
		#자르는 횟수보다 크거나 같으면 줄여야 되니 앞을 댕겨
		#이부분이 이해가 안된다..
		if total >= i+1: #여기서 왜 +1을?
			S = mid+1
			if max_mid < mid:
				max_mid = mid
		else:
			E = mid - 1	
	
	#한턴이 끝나면 정답 list에 넣어주고, max_mid 초기화
	result_list.append(max_mid)
	max_mid = 0
	S = 1
	E = 4000000 #L 이어도 되지 않을까?
	max_mid = 0

for i in result_list:
	print(i)
