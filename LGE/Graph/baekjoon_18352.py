#https://www.acmicpc.net/problem/18352

import sys
from collections import deque
import math

input = sys.stdin.readline
#sys.maxsize int 형 변수의 최대 크기
#print(f"[+][sung] ")

flag = 0
N, M, K, X = map(int, input().split())
# N, M, K, X = map(int, sys.stdin.readline().split())

data_list = [[] for i in range(N+1)]

for i in range(M):
	s, e = map(int, input().split())
	data_list[s].append(e)
	
visited = [math.inf]*(N+1)

q = deque()
q.append([X, 0])
visited[X] = 0

while q:
	node, cost = q.popleft()
	
	if visited[node] < cost:
		continue
	
	for idx, data in enumerate(data_list[node]):
		# print(f"[+][sung] data = {data}")
		next_node = data
		next_edge = 1

		if visited[next_node] > visited[node] + next_edge:
			visited[next_node] = visited[node] + next_edge
			q.append([next_node,  visited[node] + next_edge])
		
for idx, data in enumerate(visited):
	# print(f"[+][sung] idx, data = {idx, data}")
	if data is K:
		print(idx)
		flag = flag+1

if flag == 0:
	print(-1)
