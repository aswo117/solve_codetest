# 그래프 문제
# 기본 문법이 부족함
# ex1. dic 선언 방법 = dict = {}, dict[(#tuple)] = 1
# ex2. list copy 시 data를 copy 하고 싶으면 .copy()를 사용하던지 인자값을 직접 넣자
# ex3. tuple은 append를 제공하지 않음

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    A,B,C,D = map(int,readl().split())
    return A,B,C,D
 
sol = -1
# 입력함수
A,B,C,D = Input_Data()

# 여기서부터 작성
q = deque()
q.append([A, B, C, D, 0])
check = {}
check[(A, B, C, D)] = 1

while q:
	data_list = q.popleft()
	
	if data_list[0] == data_list[1] == data_list[2] == data_list[3]:
		sol = data_list[4]
		break
	else:
		for i in range(4):
			for j in range(4):
				if data_list[i] < data_list[j]:
					fix_data = data_list[i] // 2
					fix_data_list = data_list.copy()
					fix_data_list[i] = fix_data_list[i] + fix_data
					fix_data_list[j] = fix_data_list[j] - fix_data
					
					check_tuple = (fix_data_list[0], fix_data_list[1], fix_data_list[2], fix_data_list[3])
					# check_tuple.append(fix_data_list[0], fix_data_list[1], fix_data_list[2], fix_data_list[3])
					
					if check_tuple in check:
						continue
					else:
						check[(check_tuple)] = 1
						q.append([fix_data_list[0], fix_data_list[1], fix_data_list[2], fix_data_list[3], data_list[4] + 1])

# 출력
print(sol)
