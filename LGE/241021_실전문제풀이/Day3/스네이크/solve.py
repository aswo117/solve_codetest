#상 하 좌 우를 너무 햇갈림
#dirction = ((-1, 0), (1, 0), (0, -1), (0, 1)) # fixed) 이게 상 하 좌 우 임. 
#sung[세로][가로] = sung[y][x] = sung [][] 
#먹은 먹이를 처리 안해줘서 문제가 됬음.
#que.popleft 하면 꼬리가 튀어나옴 (1)(2)(3)(머리) 면 popleft 하면 (1)이 튀어나오는 거임. 
#우린 머리로 계산했어야 했으니, q[-1]로 해야함.

import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	K = int(readl())
	pos = [tuple(map(int, readl().split())) for _ in range(K)]
	L = int(readl())
	cmd_list = [list(readl().split()) for _ in range(L)]
	cmd_list = [[int(c[0]),c[1]] for c in cmd_list]

	return N, K, pos, L, cmd_list

sol = -1
# 입력받는 부분
N, K, pos, L, cmd_list = Input_Data()

# 여기서부터 작성
maps = [[0 for i in range(0, N+1)] for j in range(0, N+1)]
# print(f"N, K, pos, L, cmd_list = {N, K, pos, L, cmd_list}")
# print(maps)
for i in range(K):
	maps[pos[i][0]][pos[i][1]] = 1

# 상 하 좌 우
# dirction = ((0, -1), (0, 1), (-1, 0), (1, 0)) Err
dirction = ((-1, 0), (1, 0), (0, -1), (0, 1)) # fixed) 이게 상 하 좌 우 임. 
cur_direction = 'R'

# 오른쪽인데 D면 아래 / L면 위
# 왼쪽인데 D면 위    / L면 아래
# 위인데 D면 오른쪽  / L면 왼쪽
# 아래인데 D면 왼쪽  / L면 오른쪽

#꼬리관리는 que로 해라?
cnt = 0
cmdlist_cnt = 0
# cur_pos = [(1, 1)]
q = deque()
q.append((1, 1)) # 꼬리관리
while 1:
	# x, y = q.popleft() 꼬리임. 제거하면 안됨
	x, y = q[-1] #머리임.
	cnt = cnt + 1
	if cur_direction == 'U':
		nx, ny = x+dirction[0][0], y+dirction[0][1]
	elif cur_direction == 'D':
		nx, ny = x+dirction[1][0], y+dirction[1][1]
	elif cur_direction == 'L':
		nx, ny = x+dirction[2][0], y+dirction[2][1]
	elif cur_direction == 'R':
		nx, ny = x+dirction[3][0], y+dirction[3][1]
	
	# print(f"cnt = {cnt}, x, y = {x, y}, nx, ny = {nx, ny}, cur_direction = {cur_direction}")
	
	# if 이동하는 좌표가 벽 혹은 자기 좌표면:
	if not (1<=nx<N+1) or not (1<=ny<N+1) or ((nx, ny) in q):
		sol = cnt
		break
	# 변경해야 되는 초가 다가오면 (cnt)
	# print(f"cmd_list[cmdlist_cnt] = {cmd_list[cmdlist_cnt]}")
	if cnt == cmd_list[cmdlist_cnt][0]:
		# print(f"cnt = {cnt}, cmdlist_cnt = {cmdlist_cnt}, cmd_list[cmdlist_cnt] = {cmd_list[cmdlist_cnt]}")
		# if 내가 U인데 변경좌표가 L이면:
		if cur_direction == 'U' and cmd_list[cmdlist_cnt][1] == 'L':
		# 	왼쪽으로 이동 변경
			cur_direction = 'L'
		# if 내가 U인데 변경좌표가 D면:
		elif cur_direction == 'U' and cmd_list[cmdlist_cnt][1] =='D':
		# 	오른쪽
			cur_direction = 'R'
		# if 내가 D인데 변경좌표가 L이면:
		elif cur_direction == 'D' and cmd_list[cmdlist_cnt][1] == 'L':
		# 	오른쪽
			cur_direction = 'R'
		# if 내가 D인데 변경좌표가 D면:
		elif cur_direction == 'D' and cmd_list[cmdlist_cnt][1] == 'D':
		# 	왼쪽
			cur_direction = 'L'
		# if 내가 L인데 변경좌표가 L이면:
		elif cur_direction == 'L' and cmd_list[cmdlist_cnt][1] == 'L':
		# 	아래
			cur_direction = 'D'
		# if 내가 L인데 변경좌표가 D면:
		elif cur_direction == 'L' and cmd_list[cmdlist_cnt][1] == 'D':
		# 	위
			cur_direction = 'U'
		# if 내가 R인데 변경좌표가 L이면:
		elif cur_direction == 'R' and cmd_list[cmdlist_cnt][1] == 'L':
		# 	위
			cur_direction = 'U'
		# if 내가 R인데 변경좌표가 D면:
		elif cur_direction == 'R' and cmd_list[cmdlist_cnt][1] == 'D':
		# 	아래
			cur_direction = 'D'
		#처리가 끝나면 다음 cmdlist로 가게 해줌
		cmdlist_cnt = cmdlist_cnt+1

	# if 이동하는 좌표에 먹이가 없으면:
	if maps[nx][ny] == 0 and q:
		q.popleft()
	#먹이가 잇으면
	maps[nx][ny] = 0 # Err 먹은 먹이 처리해줘야 함.
	q.append((nx, ny))
	
	# print(f"q = {q}")
# 출력하는 부분
print(sol)
