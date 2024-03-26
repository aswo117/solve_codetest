from collections import deque

Escaped_flag = False

while(1):
	NZ, NX, NY = map(int, input().split())
	if NZ == 0 and NX == 0 and NY == 0:
		break;
	# print(f"NZ ,NX, NY = {NZ, NX, NY}")
	q = deque()

	maps2 = [0]*NZ
	s_index = []
	e_index = [] #필용벗음

	# print(q)
	def print_maps():
		for z in range(NZ):
			for i in range(NX):
				print(f"{maps2[z][i]}")
			print(f" ")

	#입력값 받고, S, E 찾기
	for z in range(NZ):
		maps = [[0 for col in range(NY)] for row in range(NX)]
		for i in range(NX+1):
			temp = list(map(str, input()))
			if(temp == []):
				maps2[z] = maps
			elif 'S' in temp:
				s_index = [z, i, temp.index('S')]
				# print(f"S index = {s_index}")
				q.append((z, i, temp.index('S'), 1))
				maps[i] = temp
			elif 'E' in temp:
				e_index = [z, i, temp.index('E')]
				# print(f"e index = {e_index}")
				maps[i] = temp
			else:
				maps[i] = temp

	maps2[int(s_index[0])][int(s_index[1])][int(s_index[2])] = 1

	# print_maps()
	
	#탐색
	while q:
		z, x, y, d = q.popleft()
		for dz, dx, dy in((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
			nz, nx, ny = z + dz, x + dx, y + dy
			if not (0<=nz<NZ) or not (0<=nx<NX) or not (0<=ny<NY):
				continue
			if maps2[nz][nx][ny] != '.':
				if maps2[nz][nx][ny] == 'E':
					maps2[nz][nx][ny] = d
					print(f"Escaped in {maps2[nz][nx][ny]} minute(s).")
					q.clear()
					Escaped_flag = True
					break
				continue

			maps2[nz][nx][ny] = d + 1
			q.append((nz, nx, ny, d+1))
			
	if Escaped_flag is False:
		print(f"Trapped!")
		q.clear()
	Escaped_flag = False
		


	#출력
	# print_maps()
