# queue
# 10, 11 timeout
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
 
def input_data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    first_second = [list(map(int,readl().split())) for _ in range(N)]
    return N, M, first_second
 
 
# 입력 받는 부분
N, M, first_second = input_data()


visited = []
q = deque()
check_count = 0
idx = 0
sol = [0]*N

 
# 코드를 작성하세요
for i in range(N):
	q.append(first_second[i])

while q:	
	for i in range(len(q)):
		if check_count == M:
			# sol[idx] = check_count
			# idx = idx+1
			# check_count = 0
			# q.popleft()
			# visited.clear()
			# print(f"check point == M")
			break
		for j in range(2):
			# print(f"q[{i}][{j}] = {q[i][j]}")
			if q[i][j] not in visited:
				# print(q[i][j])
				visited.append(q[i][j])
				check_count = check_count + 1
				# print(f"check_count = {check_count}")
				break
		
	sol[idx] = check_count
	idx = idx+1
	check_count = 0
	q.popleft()
	visited.clear()
 
# 출력 하는 부분
print(*sol,sep='\n')
