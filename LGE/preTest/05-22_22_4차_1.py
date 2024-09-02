#05-22_22_4차
#1 (OK)
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
import math
 
def input_data():
    readl = sys.stdin.readline
    a = readl()
    return a
 
def solve():
    ans = 0
    for i in range(0,len(A)-1):
        if A[i] == '(' and A[i+1] == ')': ans+=1
	
    return ans
                         
# 입력
# A : 핫도그 꽂을 자리 정보

def solve2(N):
	data = 0
	while N >= 1:
		data = data + (N-1)
		N = N-1
	
	return data
	

#경우의 수 출력하면됨.

sol = -1
A = input_data()
sol = solve()
sol2 = solve2(sol)
# print(sol)
print(sol2)
