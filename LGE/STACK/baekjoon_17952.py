#https://www.acmicpc.net/problem/17952

import sys
import math
from collections import deque

N = int(input())

data_list = list()
stack_list = list()
for i in range(N):
	data_list.append(list(map(int, input().split())))
	
total_score = 0
	
for i in range(N):
	# print(f"i = {i}")
	# print(f"data_list[i] = {data_list[i]}")
	if data_list[i] == [0]:
		# print(f"stack_list[-1] = {stack_list[-1]}")
		if not stack_list:
			continue
		else:
			stack_list[-1][1] = stack_list[-1][1] -1
			if stack_list[-1][1] == 0:
				total_score = total_score + stack_list[-1][0]
				stack_list.pop()
	else:
		# print(f"data_list[i][1] = {data_list[i][1]}, data_list[i][2] = {data_list[i][2]}")
		append_list = [data_list[i][1], data_list[i][2]-1]
		# print(f"append_list = {append_list}")
		if append_list[1] == 0:
			total_score = total_score + append_list[0]
		else:
			stack_list.append(append_list)
		
print(total_score)
		
