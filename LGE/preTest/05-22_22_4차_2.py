# List 의 총 합 구하기 sum()
# list 자체가 stack, pop()을 쓰면 그냥 stack이다
# sort 할때 stack.sort(reverse=True) 로 하면 내림차순
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
input = sys.stdin.readline

data_list = list()
N = int(input())
for i in range(N):
	X, Y = map(int, input().split())
	data_list.append([X, Y])

data_list.sort()
stack = list()
total_cost = 0

# print(data_list)

for i in range(N):
	# print(f"[+][sung] data_list[i][1] = {data_list[i][1]}")
	if not stack:
		stack.append(data_list[i][1])
	else:
		while 1:
			if not stack or data_list[i][1] >= stack[-1]: #새로 들어온 data값이 stack 최상단 값보다 크면
				stack.append(data_list[i][1])
				break
			else:
				total_cost = total_cost + data_list[i][1]
				stack.pop()
	
	# print(stack)
	# print(f"[+][sung] total_cost = {total_cost}")


print(total_cost + sum(stack))
