#https://www.acmicpc.net/problem/5014
#70% Fail -> OK
#BFS에서 append를 하고나서 visited를 해주자
#graph(BSF)로 문제를 풀면 가지치기 하지말고 vistied로만 처리하자

import sys
from collections import deque
import math

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visited = [-1]*(F+1)

flag = -1
currnt = S
q = deque()
q.append(S)
visited[S] = 0

while q:
	current = q.popleft()
	# print(current, visited[current])
	if current == G:
		print(visited[current])
		flag = 1
		break
		
	for i in (current+U, current-D):
		# print(f"[+][sung] i = {i}")
		# print(f"[+][sung] visited[i] = {visited[i]}")
		if (not 0 < i <= F) or (visited[i] != -1):
			# print("[+][sung] continue")
			continue
		else:
			q.append(i)
			visited[i] = visited[current] + 1
	
if flag == -1:
	print("use the stairs")		
