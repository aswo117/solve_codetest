#https://www.acmicpc.net/problem/2805 (Pass)

import sys
from collections import deque
import math

input = sys.stdin.readline

N, M = map(int, input().split())
data_list = list(map(int, input().split()))

S = 0
E = 1000000000
max_tree = math.inf
sol = -1

def check(m):
	temp = 0
	# print(f"[+][sung] m = {m}")
	for i in data_list:
		if i - m > 0:
			# print(f"[+][sung] {i} - {m} = {i-m}")
			temp = temp + i - m
			# print(f"[+][sung] temp = {temp}")	
		else:
			continue
	return temp

while S <= E:
	mid = (S+E)//2
	total = check(mid)

	if total >= M:
		S = mid+1
		if max_tree > total:
			max_tree = total
			sol = mid
	else:
		E = mid-1

print(sol)
		
