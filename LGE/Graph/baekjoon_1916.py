#https://www.acmicpc.net/problem/1916

import sys
from collections import deque
import math

#input = sys.stdin.readline 이렇게 변환해서 쓰기도 하네
#sys.maxsize int 형 변수의 최대 크기
#print(f"[+][sung] ")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

data_list = [[] for i in range(N+1)]

for i in range(M):
	s, e, c = map(int, sys.stdin.readline().split())
	data_list[s].append((e, c))
start, end = map(int, sys.stdin.readline().split())

visited = [math.inf]*(N+1)

q = deque()
q.append([start, 0])
visited[start] = 0

while q:
	node, cost = q.popleft()
	
	if visited[node] < cost:
		continue
	
	# print(f"data_list = {data_list}")
	# print(f"data_list[node] = {data_list[node]}")
	# print(f"data_list[node][0] = {data_list[node][0]}")
	
	for idx, data in enumerate(data_list[node]):
		next_node = data[0]
		next_edge = data[1]
		
		# print(f"[+][sung] next_node = {next_node}")
		# print(f"[+][sung] next_edge = {next_edge}")
		# print(f"[+][sung] visited[next_node] = {visited[next_node]}")
		
		if visited[next_node] > visited[node] + next_edge:
			visited[next_node] = visited[node] + next_edge
			q.append([next_node, visited[node] + next_edge])

print(visited[end])
