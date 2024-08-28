#https://www.acmicpc.net/problem/1654
#1 2 
#1 입력이 안됨..

import sys
from collections import deque

input = sys.stdin.readline

K, N = map(int, input().split())
data_list = list()
for i in range(K):
	data_list.append(int(input()))

# print(data_list)

#크기를 return 해야
def check(m):
	# print(f"[+][sung] check start m = {m}")
	temp_total = 0
	for i in data_list:
		# print(f"[+][sung] i = check the {i}")
		if i-m>=0:
			# print(f"[+][sung] start = {i}, m = {m}")
			while i-m >= 0:
				# print(f"[+][sung] before i = {i}")
				temp_total = temp_total + 1
				i = i-m
				# print(f"[+][sung] after i = {i}")
			else:
				continue
	
	return temp_total	
	
S = 0
E = 1000000
max_mid = 0

while S<=E:
	mid = (S+E)//2
	total = check(mid)
	
	# print(f"[+][sung] total = {total}, mid = {mid}, max_mid = {max_mid}")
	if total >= N:
		S = mid+1
		if max_mid < mid:
			max_mid = mid
	else:
			E = mid-1

print(max_mid)
