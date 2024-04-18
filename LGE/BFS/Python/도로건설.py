#https://swedu.lge.com/
#성공
import sys
from collections import deque

q = deque()
maps = []

def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	map_cost = [
		[0] + list(map(int, readl()[:-1])) + [0] if 1 <= r <= N else [0] * (N + 2)
		for r in range(N + 2)
	]
	return N, map_cost

sol = -2

# 입력받는 부분
N, map_cost = input_data()

# 여기서부터 작성

def print_maps():
	for i in range(N):
			print(maps[i])
			
def print_map_cost():
	for i in range(N+2):
			print(map_cost[i])
			
maps = [[0 for i in range(N)] for j in range(N)]
q.append((0, 0, 0))

# print_maps()
# print_map_cost()

while q:
	x, y, d = q.popleft()
	for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
		nx, ny = x+dx, y+dy
		if not(0<=nx<N) or not(0<=ny<N):
			continue
		
		new_cost = maps[x][y] + map_cost[nx+1][ny+1]
		# print(f"[+][sung] x = {x}, y = {y}, nx = {nx} ny = {ny}")
		# print(f"[+][sung] new_cost = {new_cost}")
		# print(f"[+][sung] cur_cost = {maps[nx][ny]}")
		if maps[nx][ny] == 0:
			maps[nx][ny] = new_cost
			q.append((nx, ny, new_cost))
		elif new_cost < maps[nx][ny]:
			maps[nx][ny] = new_cost
			# print(f"[+][sung] change cost")
			# print_maps()
			q.append((nx, ny, new_cost))

# 출력하는 부분

# print_maps()
sol = maps[N-1][N-1]
print(sol)
