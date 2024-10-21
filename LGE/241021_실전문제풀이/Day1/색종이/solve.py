# 쓸대없이 BFS로 풀려고 했던 문제
# Map 을 만들어주고 1로 채운 후 1일 때 위 아래 좌 우 가 1이면 외각선임을 이용한다

import sys 
from collections import deque

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    info = [list(map(int, readl().split())) for _ in range(N)] 
    return N, info 

sol = 0 

# 입력받는 부분 
N, info = input_data() 

maps = [[0 for i in range(101)] for j in range(101)]
q = deque()

#fill paper
# for i in range(N):
# 	for j in range(10):
# 		# print(f"info[i][0]+j, info[i][1]+j = {info[i][0]+j, info[i][1]+j}")
# 		if info[i][0]+j < 101 or info[i][1]+j < 101:
# 			maps[info[i][0]+j][info[i][1]+j] = 1
for sc, sr in info:
				for r in range(sr, sr + 10):
								for c in range(sc, sc + 10):
												maps[r][c] = 1

for x in range(1, 100):
	for y in range(1, 100):
		if maps[x][y] == 0:
			continue
		for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
			nx, ny = x+dx, y+dy	
			if (not 0<=nx<101) or (not 0<=ny<101) or (maps[nx][ny] == 0):
				sol = sol+1
				
print(sol)
