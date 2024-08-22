#https://www.acmicpc.net/problem/5014
#70% Fail

import sys
from collections import deque
import math

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visited = [math.inf]*(F+U+1)
count = 0
flag = 0
current = 0

q = deque()
q.append(S)
visited[S] = 1

while q:
	current = q.popleft()
	visited[current] = 1
		
	if current == G:
		flag = 1
		print(count)
		break;
	else:
		if current <= G:
			if current+U <= F and visited[current+U] != 1:
				count = count+1
				current = current+U
				q.append(current)	
			elif current-D > 0:
				if visited[current-D] != 1:
					count = count+1
					current = current-D
					q.append(current)
			else:
				flag = -1
				break
		else:
			if current-D > 0:
				if visited[current-D] != 1:
					count = count+1
					current = current-D
					q.append(current)
			elif current+U <= F and visited[current+U] != 1:
				count = count+1
				current = current+U
				q.append(current)
			else:
				flag = -1
				break

if flag == -1:
	print("use the stairs")
