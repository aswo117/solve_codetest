#https://www.acmicpc.net/board/view/132035 반례

from collections import deque

N = int(input())
q_distance = deque()
q_feed = deque()
maps_feed = []
maps_distance = []
shark_size = 2
shark_feed = 0
shark_distance = 0
call_mam = True

next_distance = 9999
next_x = 0
next_y = 0

def print_data():
	print(f"next start feed = {next_x, next_y}")
	print(f"shark_distance, shark_size, shark_feed = {shark_distance, shark_size, shark_feed}")
	print("distance")
	for i in range(N):	
		print(maps_distance[i])
	print("feed")
	for i in range(N):
		print(maps_feed[i])
	print()

def calculate_distance():
	maps_distance[next_x][next_y] = 1
	while q_distance:
		x, y, d = q_distance.popleft()
		for dx, dy in((-1, 0), (1, 0), (0, -1), (0, 1)):
			nx, ny = x+dx, y+dy
			if not (0<=nx<N) or not (0<=ny<N):
				continue
			if maps_distance[nx][ny] != 0 or maps_feed[nx][ny] > shark_size:
				continue
			maps_distance[nx][ny] = d + 1
			q_distance.append((nx, ny, d+1))

#여기가 이상
def find_feed():
	global next_x, next_y, next_distance, shark_distance, shark_size, shark_feed, call_mam
	for i in range(N):
		for j in range(N):
			if maps_feed[i][j] != 0 and maps_feed[i][j] < shark_size:
				q_feed.append((i, j, maps_distance[i][j]))
	print(f"q_feed = {q_feed}")
	if q_feed:
		while q_feed:
			x, y, d = q_feed.popleft()
			print(f"x, y, d = {x, y, d}")
			#거리가 작은게 우선
			if next_distance > d and d != 0:
				next_x = x
				next_y = y
				next_distance = d
				print(f"next_distance = {next_distance}")
			else:
				continue
			# elif next_feed == d: pass
		# print(f"next_x = {next_x} next_y = {next_y}")
		maps_feed[next_x][next_y] = 0	#0으로 초기화
		shark_feed = shark_feed+1
		if shark_feed == shark_size:
			shark_size = shark_size+1
			shark_feed = 0		
		if next_distance != 9999:
			shark_distance = shark_distance+next_distance-1
			print(f"shark_distance = {shark_distance}")
			next_distance = 9999
	else:
		call_mam = False
		# print("call mam")

def clear_data():
	for i in range(N):
		for j in range(N):
			maps_distance[i][j] = 0

#초기값 입력 받기
for i in range(N):
	maps_feed.append(list(map(int, input().split())))
for i in range(N):
	maps_distance.append(list([0]*N))
for i in range(N):
	if 9 in maps_feed[i]:
		q_distance.append((i, maps_feed[i].index(9), 1))
		# maps_distance[i][maps_feed[i].index(9)] = 1
		next_x = i
		next_y = maps_feed[i].index(9)
		maps_feed[i][maps_feed[i].index(9)] = 0
		break

while(call_mam):
	print(f"q_distance = {q_distance}")
	calculate_distance()	#거리계산
	find_feed()	#먹이 계산 및 길찾기
	q_distance.append((next_x, next_y, 1))	#다음 좌표 입력
	print_data()
	clear_data()

	

