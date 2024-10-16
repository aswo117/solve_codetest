# TC3, 8 Fail

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
#상 하 좌 우
#[-1, 1, -1, 1]

def check_pip(pip, check_value):
	if pip == 0:
		pip_road = ((0, 0))
	elif pip == 1:
		pip_road = ((-1, 0),(1, 0))
	elif pip == 2:
		pip_road = ((0, -1),(0, 1))
	elif pip == 3:
		pip_road = ((0, 1),(1, 0))
	elif pip == 4:
		pip_road = ((-1, 0),(0, 1))
	elif pip == 5:
		pip_road = ((-1, 0),(0, -1))
	elif pip == 6:
		pip_road = ((0, -1),(1, 0))
	elif pip == 7:
		pip_road = ((0, -1),(1, 0),(0, 1))
	elif pip == 8:
		pip_road = ((-1, 0),(0, 1),(1, 0))
	elif pip == 9:
		pip_road = ((-1, 0),(0, -1),(0, 1))
	elif pip == 10:
		pip_road = ((-1, 0),(0, -1),(1, 0))
	elif pip == 11:
		pip_road = ((-1, 0),(0, -1),(0, 1),(1, 0))
	
	if check_value in pip_road:
		return True
	else:
		return False

def input_data():
	N = int(input())
	sc, sr = map(int, input().split())
	sc += 1
	sr += 1
	map_city = [
		[0] + list(map(int, input(), [16] * (N))) + [0]
		if 1 <= r <= N
		else [0] * (N + 2)
		for r in range(N + 2)
	]
	return N, sc, sr, map_city


sol = 0
# 입력받는 부분
N, sc, sr, map_city = input_data()
q = deque()

# print(f"N, sc, sr, map_city = {N, sc, sr, map_city}")
# 여기서부터 작성

maps = [[0 for i in range(N)] for j in range(N)]
q.append([sc, sr])
maps[sc-1][sr-1] = 1

# print(maps)
# print(map_city)

while q:
	x, y = q.popleft()
	for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):		
		nx, ny = dx+x, dy+y
		# print(f"x, y = {x, y}")
		# print(f"nx, ny = {nx, ny}")
		if not (1<=nx<N+1) or not (1<=ny<N+1):
			continue
		# print(f"maps[nx][ny] = {maps[nx][ny]}")
		if maps[nx-1][ny-1] != 0:
			continue
		
		# print(f"dx, dy = {dx, dy}")
		#x가 상하, y가 좌우
		#상
		result = -1
		if dx == -1 and dy == 0: #(0, 1) check
			if check_pip(map_city[x][y], (0, -1)) is True and check_pip(map_city[nx][ny], (0, 1)) is True:
				result = 1
		#하
		elif dx == 1 and dy == 0: #(0, -1) check
			if check_pip(map_city[x][y], (0, 1)) is True and check_pip(map_city[nx][ny], (0, -1)) is True:
				result = 1
		#좌
		elif dx == 0 and dy == -1: #(1, 0) check
			if check_pip(map_city[x][y], (-1, 0)) is True and check_pip(map_city[nx][ny], (1, 0)) is True:
				result = 1
		#우
		elif dx == 0 and dy == 1: #(-1, 0) check
			if check_pip(map_city[x][y], (1, 0)) is True and check_pip(map_city[nx][ny], (-1, 0)) is True:
				result = 1
		
		# print(f"result = {result}")
		if result == -1:
			continue
		else:
			# print(f"x, y = {x, y}")
			# print(f"dx, dy = {dx, dy}")
			# print(f"nx, ny = {nx, ny}")
			maps[nx-1][ny-1] = 1
			q.append([nx, ny])

#출력하는 부분
for i in range(N):
	for j in range(N):
		if maps[i][j] == 0 and map_city[i+1][j+1] != 0:
			sol = sol+1
			
print(sol)
# print(maps)
