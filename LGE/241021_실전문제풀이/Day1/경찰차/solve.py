# DFS 문제
# 완전 탐색 중 모든 경우의 수를 구해야 되는 경우 DFS 사용
# Stack과 recursive 두 방법으로 DFS구현이 가능하나 Stack이 오히려 더 어려우니 걍 Recursive로 풀자
# 변화해야 되는 값들을 DFS 인자값으로 넣어주는게 Key Point

import sys
import math
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	W = int(readl())
	pos = [list(map(int, readl().split())) for n in range(W)]
	return N, W, pos

sol = -1
# 입력받는 부분
N, W, pos = Input_Data()
 
# 여기서부터 작성
# print(f"N, W, pos = {N, W, pos}")
 
min_distance = int(1e9)
 
def dfs(step, first_p, second_p, total_distance):
	global min_distance
	if step > W-1:
		if min_distance > total_distance:
			min_distance = total_distance
			# print(f"return step {step}")
		return
	# print(f"** pos[step] = {pos[step]} **")
	# print(f"first_p = {first_p}")
	# print(f"abs(first_p[0]-pos[step][0]) + abs(first_p[1]-pos[step][1]) = {total_distance + abs(first_p[0]-pos[step][0]) + abs(first_p[1]-pos[step][1])}")
	# print(f"second_p = {second_p}")
	# print(f"abs(second_p[0]-pos[step][0]) + abs(second_p[1]-pos[step][1]) = {total_distance + abs(second_p[0]-pos[step][0]) + abs(second_p[1]-pos[step][1])}")

	dfs(step+1, pos[step], second_p, total_distance + abs(pos[step][0]-first_p[0]) + abs(pos[step][1]-first_p[1]))
	dfs(step+1, first_p, pos[step], total_distance + abs(pos[step][0]-second_p[0]) + abs(pos[step][1]-second_p[1]))

dfs(0, [1, 1], [N, N], 0)

# 출력하는 부분
print(min_distance)
