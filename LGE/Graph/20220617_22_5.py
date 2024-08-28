#부품 이동 전략 설정
#1, 2, 5, 11만 Pass -> -2 return 값이 문제 -> Pass

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from collections import deque
import math
def Input_Data():
    readl = sys.stdin.readline
    A,B,C,D = map(int,readl().split())
    return A,B,C,D
 
sol = -1

# 입력함수
A,B,C,D = Input_Data()
check = {}

q = deque()
# q.insert(A, B, C, D)
q.append([A, B, C, D, 0])
check[(A, B, C, D)] = 1

# print(f"[+][sung] q = {q}")
#print(f"[+][sung] check = {check}")

while q:
	data_list = q.popleft()
	# print(f"[+][sung] data_list = {data_list}")
	
	if data_list[0] == data_list[1] == data_list[2] == data_list[3]:
		# print("[+][sung] break")
		# print(f"[+][sung] data_list = {data_list}")
		sol = data_list[4]
		break
		# if(sol < data_list[4]):
			# sol = data_list[4]
	for idx_1, data_1 in enumerate((data_list[0], data_list[1], data_list[2], data_list[3])):
		for idx_2, data_2 in enumerate((data_list[0], data_list[1], data_list[2], data_list[3])):
			if data_1 >= data_2:
				continue
			else:				
				check_data_list = [data_list[0], data_list[1], data_list[2], data_list[3]]
				# check_data_list[idx_1] = check_data_list[idx_1] + int(check_data_list[idx_1]/2)
				# check_data_list[idx_2] = check_data_list[idx_2] - int(check_data_list[idx_1]/2)
				
				cal_value = int(check_data_list[idx_1]/2)
				check_data_list[idx_1] = check_data_list[idx_1] + cal_value
				check_data_list[idx_2] = check_data_list[idx_2] - cal_value
				
#				print(f"[+][sung] data_list = {data_list}")
				check_data_tuple = (check_data_list[0], check_data_list[1], check_data_list[2], check_data_list[3])
				if check_data_tuple in check:
					# print(f"continue, check_data = {check_data_tuple}, check = {check}")
					continue
				else:
					check[check_data_tuple] = 1
					q.append([check_data_list[0], check_data_list[1], check_data_list[2], check_data_list[3], data_list[4]+1])
 
# 여기서부터 작성
 
# 출력
print(sol)
