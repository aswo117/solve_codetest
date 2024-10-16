#https://www.acmicpc.net/problem/2206
#pass

import sys
from collections import deque
import math

N, M = map(int, input().split())
maps = []
q = deque()
# visitied = [[[0 for i in range(N+1)] for j in range(M+1)] for z in range(3)]
visitied = [[[0] * 2 for _ in range(M)] for _ in range(N)]
# print(visitied)
# print(visitied)
for i in range(N):
	maps.append(list(input()))

q.append([0, 0, 0])
visitied[0][0][0] = 1

min_result = 1000000

while q:
	x, y, b = q.popleft()
	# print(x, y, b)
	if x == N-1 and y == M-1 and b < 2:
		if visitied[x][y][b] < min_result:
			# print(f"b, visitied[x][y][b] = {b}, {visitied[x][y][b]}")
			min_result = visitied[x][y][b]
	for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
		nx, ny = dx+x, dy+y
		if not (0<=nx<N) or not (0<=ny<M):
			continue
		if visitied[nx][ny][b] != 0:
			continue
		# print(f"nx, ny, maps[nx][ny] = {nx, ny, maps[nx][ny]}")
		if maps[nx][ny] == '1':
			if b == 0:
				visitied[nx][ny][b+1] = visitied[x][y][b] + 1
				q.append([nx, ny, b+1])
		else:
			visitied[nx][ny][b] = visitied[x][y][b] + 1
			q.append([nx, ny, b])
		# print(f"q = {q}")
if min_result == 1000000:
	print(-1)
else:
	print(min_result)
