#https://www.acmicpc.net/problem/2493
#OK

import sys
from collections import deque

stack = []

N = int(input())
data_list = list(map(int, input().split()))
result_list = [0]*N
idx = N-1

for i in range(N):
	while(1):
		if not stack or stack[-1][0] >= data_list[-1]:
			stack.append([data_list[-1], len(data_list)-1])
			data_list.pop()
			break
		elif stack[-1][0] < data_list[-1]:
			result_list[stack[-1][1]] = len(data_list)	
			stack.pop()

print(' '.join(map(str, result_list)))
