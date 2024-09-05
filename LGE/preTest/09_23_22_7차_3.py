# 고치니 더 틀림

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
import math

max_value = 0

def InputData():
    readl = sys.stdin.readline
    N = int(readl())
    D = [list(map(int,readl().split())) for r in range(N)]
    return N, D
 

ans = -1
min_cut_tree = math.inf
max_group_tree = 0

# 입력 함수
N, D = InputData()
# 여기서부터 작성
# print(N, D)

for i in range(N):
	if max_value < max(D[i]):
		max_value = max(D[i])

# visited = [[0]*N for i in range(N)]
q = deque()
# visited = [[0 for i in range(N)] for j in range(N)]

# print(visited)
for cut in range(max_value):
	visitied = [[0]*N for i in range(N)]	
	group_tree = 0
	cut_tree = 0
	# print(f"[+][sung] ==== {cut} ==== ")

	for x in range(N):
		for y in range(N):
			# print(x, y)
			if D[x][y] <= cut:
				cut_tree = cut_tree + 1
				# print(f"[{x}][{y}]")
				# print(f"[+][sung] cut tree = {cut_tree}")
				continue
			if visitied[x][y] == 1:
				continue
			
			q = deque()
			q.append((x, y))
			visitied[x][y] = 1
			group_tree = group_tree + 1

			while q:
				x, y = q.popleft()
				for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
					nx, ny = x + dx, y + dy
					if not (0<=nx<N) or not (0<=ny<N):
						continue
					if D[nx][ny] <= cut:
						continue
					if visitied[nx][ny] == 1:
						continue
					
					visitied[nx][ny] = 1
					q.append((nx, ny))
	
	# print(f"[+][sung] cut = {cut}")
	# print(f"[+][sung] group_tree = {group_tree}")
	# print(f"[+][sung] cut_tree = {cut_tree}")
	if max_group_tree < group_tree:
		max_group_tree = group_tree
		min_cut_tree = cut_tree
	elif max_group_tree == group_tree:
		if min_cut_tree > cut_tree:
			min_cut_tree = cut_tree
# 출력
print(min_cut_tree)
