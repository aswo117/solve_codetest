# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

q = deque()
maps = []

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

def check_pip(pip, check_value):
	# print(f"[+][sung] pip = {pip}, check_value = {check_value}")
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
	
	# print(f"[+][sung] pip_road = {pip_road}, check_value = {check_value}")
	if check_value in pip_road:
		# print("return True")
		return True
	else:
		# print("return False")
		return False

sol = 0
# 입력받는 부분
N, sc, sr, map_city = input_data()
# 여기서부터 작성

maps = [[0 for i in range(N)] for j in range(N)]
maps[sr-1][sc-1] = 1
q.append((sc-1, sr-1, 1))


while q:
	x, y, d = q.popleft()
	# print(x, y, d)
	# print(maps)
	for dx, dy in((-1, 0), (1, 0), (0, -1), (0, 1)): #상 하 좌 우
		nx, ny = x+dx, y+dy
		if not(0<=nx<N) or not(0<=ny<N):
			# print(f"[+][sung] ({dx},{dy}) ({nx}, {dy}) continue 1")
			continue
		if maps[nx][ny] != 0:
			# print(f"[+][sung] ({dx},{dy}) ({nx}, {dy}) continue 2")
			continue
		#검출 알고리즘
		# print(f"[+][sung] dx = {dx}, dy = {dy}")
		if dx == -1 and dy == 0: #상
			if (check_pip(map_city[x+1][y+1], (0, -1)) is True) and (check_pip(map_city[nx+1][ny+1], (0, 1)) is True):
					maps[nx][ny] = d + 1
					q.append((nx, ny, d+1))
		elif dx == 1 and dy == 0: #하
				if (check_pip(map_city[x+1][y+1], (0, 1)) is True) and (check_pip(map_city[nx+1][ny+1], (0, -1)) is True):
					maps[nx][ny] = d + 1
					q.append((nx, ny, d+1))
		elif dx == 0 and dy == -1: #좌
				if (check_pip(map_city[x+1][y+1], (-1, 0)) is True) and (check_pip(map_city[nx+1][ny+1], (1, 0)) is True):
					maps[nx][ny] = d + 1
					q.append((nx, ny, d+1))
		elif dx == 0 and dy == 1: #우
				if (check_pip(map_city[x+1][y+1], (1, 0)) is True) and (check_pip(map_city[nx+1][ny+1], (-1, 0)) is True):
					maps[nx][ny] = d + 1
					q.append((nx, ny, d+1))
		# print(maps)
# 출력하는 부분
# print(maps)

for i in range(N):
	for j in range(N):
		if maps[i][j] == 0:
			if map_city[i+1][j+1] == 0:
				continue
			else:
				sol = sol + 1

print(sol)
# print(N, sc, sr, map_city)
