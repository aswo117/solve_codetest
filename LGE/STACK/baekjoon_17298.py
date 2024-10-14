#https://www.acmicpc.net/problem/17298
#OK

import sys
from collections import deque

stack = []

N = int(input())
data_list = list(map(int, input().split()))
result_list = []
# idx = N-1
# print(data_list)

for i in range(N):
	while 1:
		if not stack:
			stack.append([data_list[-1], -1])
			result_list.append(-1)
			data_list.pop()
		else:
			if not data_list:
				break
			if stack[-1][0] > data_list[-1]:
				result_list.append(stack[-1][0])
				stack.append([data_list[-1], stack[-1][0]])	
				data_list.pop()
				break
			else:
				if not stack:
					result_list.append(-1)
					stack.append([data_list[-1], -1])
					data_list.pop()
					break
				elif stack[-1][1] > data_list[-1]:
					result_list.append(stack[-1][1])
					stack.append([data_list[-1], stack[-1][1]])	
					data_list.pop()
					break
				else:
					# result_list.append(-1)
					# stack.append([data_list[-1], -1])
					stack.pop()
			
			
	# print(stack)

result_list.reverse()
print(' '.join(map(str, result_list)))
