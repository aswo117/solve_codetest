#상범 빌딩과 유사
#BFS

import sys
from collections import deque
 
def Input_Data():
	readl = sys.stdin.readline
	L, R, C = map(int, readl().split())
	map_dungeon = [[list(readl().strip())for r in range(R+1)] for l in range(L)]
	return L, R, C, map_dungeon

sol_list = []
sp = []
# q = deque()
flag = False

while 1:  
	# 입력 받는 부분  
	q = deque()
	L, R, C, map_dungeon = Input_Data()
	if L == 0 and R == 0 and C == 0: break
		
	# 여기서부터 작성    
	# Start 지점 찾기
	for z in range(L):
		for x in range(R):
			for y in range(C):
				if map_dungeon[z][x][y] == 'S':
					q.append((z, x, y, 0))
					break
	
	while q:
		z, x, y, v = q.popleft()
		for dz, dx, dy in ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
			nz, nx, ny = dz+z, dx+x, dy+y
			if not (0<=nz<L) or not(0<=nx<R) or not(0<=ny<C):
				continue
			if map_dungeon[nz][nx][ny] == 'E':
				# print("[sung] True!!!")
				check = v
				flag = True
				break
			if map_dungeon[nz][nx][ny] != '.':
				continue
			q.append((nz, nx, ny, v+1))
			map_dungeon[nz][nx][ny] = v+1
	# print(map_dungeon)
	if flag == True:
		print(f"Escaped in {check+1} minute(s).")
		flag = False
	else:
		print("Trapped!")
		flag = False
	

# print(f"L, R, C, map_dungeon = {L, R, C, map_dungeon}")
# print(*sol_list, sep='\n') 
