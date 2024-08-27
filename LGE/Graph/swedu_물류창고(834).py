#https://swedu.lge.com/learn/lecture/834
#물류창고

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
import math

def input_data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	infos = [list(map(int, readl().split())) for _ in range(M)]
	return N, M, infos

sol = -1

# 입력받는 부분
N, M, infos = input_data()

# 여기서부터 작성
data_list = [[] for i in range(N+1)]
max_list = []*(N+1)
visited = [math.inf]*(N+1)

for s, e, c in infos:	
	data_list[s].append((e, c))
	data_list[e].append((s, c))
	
# print(data_list)

q = deque()

for i in range(N):
	visited = [math.inf]*(N+1)
	q.append([i+1, 0])
	while q:
		node, cost = q.popleft()
		
		if visited[node] > cost:
			visited[node] = cost
		
		for idx, data in enumerate(data_list[node]):
			next_node = data[0]
			next_cost = data[1]
			
			if visited[next_node] > visited[node] + next_cost:
				visited[next_node] = visited[node] + next_cost
				q.append([next_node, visited[node] + next_cost])
				# print(visited)
	
	# print(visited)
	visited.sort(reverse=True)
	max_list.append(visited[1])
# 출력하는 부분
print(min(max_list))
