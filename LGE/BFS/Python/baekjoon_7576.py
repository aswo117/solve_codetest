from collections import deque

NY, NX = map(int, input().split())
q = deque()
maps = []
result = -1

for i in range(NX):
	maps.append(list(map(int, input().split())))

# print(f"maps = {maps}")
# print(f"maps = {maps[3][5]}")

# 1인 지점(시작지점) 찾아 deque에 넣기
for x in range(NX):
	for y in range(NY):
		# print(f"maps[{x}][{y}] == {maps[x][y]}")
		if maps[x][y] == 1:
			q.append((x, y, 1))
			
# print(f"{q}")
while q:
	x, y, d = q.popleft()
	# print(f"x, y, d = {x, y, d}")
	result = d-1
	# print(f"result = {result}")
	for dx, dy in((-1, 0), (1, 0), (0, -1), (0, 1)):
		# print(f"dx = {dx}, dy = {dy}")
		nx, ny = x+dx, y+dy
		# print(f"nx = {nx}, ny = {ny}")
		if not (0<=nx<NX) or not (0<=ny<NY):
			continue
		if maps[nx][ny] != 0:
			continue
		maps[nx][ny] = d + 1
		q.append((nx, ny, d+1))

# 0이 있으면 -1로 return
for x in range(NX):
	for y in range(NY):
		if maps[x][y] == 0:
			result = -1
			
print(f"{result}")
