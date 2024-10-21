'''
시간복잡도
최적화 관련 문제
모든 경우의 수?
DFS, BFS
DFS = 경우의 수가 많으면 시간내에 해결 못함
BFS = 최단 경로구하기, 하나만 뺴고? 이런건 쉽진 않음

sol
반복된 계산을 미리 해줌.
'''

import sys
import math

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [list(map(int,readl().split())) for _ in range(N)]
	return N, pos

sol = math.inf
# 입력 받는 부분
N, pos = Input_Data()

# 여기서부터 작성
# print(f"N, pos = {N, pos}")

result = []
for i in range(N-1):
	result.append(abs(pos[i+1][1] - pos[i][1]) + abs(pos[i+1][0] - pos[i][0]))
	
result_sum = sum(result) #전체 구간의 거리를 미리 구한 후에
# print(f"result, result_sum = {result, result_sum}")

#건너뛰는걸 구해서 뺴주면 됨.
for j in range(1, N-1):
	# target을 건너뛴 거리 = temp_dist
	temp_dist = abs(pos[j-1][1] - pos[j+1][1]) + abs(pos[j-1][0] - pos[j+1][0])
	# 건너뛴 거리를 빼고 신규 거리를 더해줌
	final_sum = result_sum + temp_dist - (result[j-1] + result[j])
	if final_sum < sol:
		sol = final_sum
		
print(sol)
	
	
	
	
	
