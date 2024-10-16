#https://www.acmicpc.net/problem/6593
#OK
import sys
from collections import deque

while 1:
	q = deque()
	maps = []
	L, R, C = map(int, input().split())
	# print(f"L, R, C = {L, R, C}")
	if L == 0 and R == 0 and C == 0:
		# print("out")
		break
	for z in range(L):
		temp = []
		for x in range(R):
			temp.append(list(input()))
		maps.append(temp)
		input()
		
	for z in range(L):
		for x in range(R):
			for y in range(C):
				if maps[z][x][y] == 'S':
					q.append([z, x, y])
					maps[z][x][y] = 0

	flag = -1
	while q:
		z, x, y = q.popleft()
		for nz, nx, ny in (((0), (0), (1)), ((0), (0), (-1)), ((0), (1), (0)), ((0), (-1), (0)), ((1), (0), (0)), ((-1), (0), (0))):
			dz, dx, dy = nz+z, nx+x, ny+y
			if not(0<=dz<L) or not(0<=dx<R) or not(0<=dy<C):
				continue
			if maps[dz][dx][dy] == 'E':
				# print(" E OK ")
				flag = maps[z][x][y]
				break
			if maps[dz][dx][dy] != '.':
				continue
			maps[dz][dx][dy] = maps[z][x][y] + 1
			q.append([dz, dx, dy])
			
	# print(maps)
			
	if flag == -1:
		print('Trapped!')
	else:
		print(f"Escaped in {flag+1} minute(s).")
