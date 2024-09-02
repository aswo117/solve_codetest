#3/11
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
# print(data_list)

# q = deque()
total_cost = 0

for i in range(N):
	# q.append(data_list[i])
	# print(f"[+][sung] q = {q}")
	
	if len(data_list) == 1:
		continue
	else:
		#data_list[i][1] 새로 들어온 값
		if data_list[i][1] >= data_list[i-1][1]: #새로 들어온 값이 기존 값보다 크거나 같을 경우
			# q.append(data_list[i]) #q에 그냥 넣어줌
			continue
		else:#새로 들어온 값이 기존 값보다 작을 경우 (update 해줘야 됨)
			#temp code, 끝까지 비교하는 코드가 들어가야됨.
			j = i-1
			while data_list[i][1] <= data_list[j][1]:
				data_list[j][1] = data_list[i][1]
				j = j -1
				if j < 0:
					break
			# q.append(data_list[i])
	
	# print(data_list)

# if len(q) == 1: #data개수가 1일 경우
# 	print(data_list[0][1])
# else:
# 	while q:
# 		dist, cost = q.popleft()
# 		print(cost)
# 		total_cost = cost + total_cost
	
# 	print(total_cost)
if len(data_list) == 1:
	print(data_list[0][1])
else:
	for i in range(N):
		total_cost = total_cost + data_list[i][1]
		
	print(total_cost)
