#floodfill

import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	#R이 세로 C가 가로
	R, C, K = map(int, readl().split())
	rects = [list(map(int,readl().split())) for _ in range(K)]
	return R, C, K, rects

sol = []

# 입력받는 부분 세로, 괄호
R, C, K, rects = Input_Data()

# 여기서부터 작성
maps = [[0 for i in range(C)] for j in range(R)]

#5 7 3
#fill_mapped
#fail
# for z in range(K):
# 	for y in range(rects[z][1], rects[z][3]):
# 		for x in range(rects[z][0], rects[z][2]):
# 			print(f"z, x, y = {z, x, y}")
# 			maps[x][y] = 1

for z in range(K):
	for r in range(rects[z][1], rects[z][3]):
		for c in range(rects[z][0], rects[z][2]):
			maps[r][c] = 1

# print(maps)		

q = deque()
for r in range(R):
	for c in range(C):
		if maps[r][c] != 0:
			continue
		else:
			q.append((r, c, 2))
			maps[r][c] = 2
			cnt = 1
			while q:
				r, c, z = q.popleft()
				for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
					nr, nc = r+dr, c+dc
					if not (0<=nr<R) or not(0<=nc<C):
						continue
					if maps[nr][nc] != 0:
						continue
					maps[nr][nc] = z + 1
					q.append((nr, nc, z + 1))
					cnt = cnt + 1
			sol.append(cnt)

# print(maps)
# 출력하는 부분 
sol.sort()
print(len(sol))
print(*sol)
