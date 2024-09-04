# 1번만 맞음..
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
 
def InputData():
    readl = sys.stdin.readline
    N = int(readl())
    A = [list(map(int,readl().split())) for _ in range(N)]
    return N, A
 
 
def Solve():
    maxint = 0
    A.sort(key = lambda x: x[0])
    start = A[0][0]
    for i in range(1, N):
        # print(f"i = {i}, A[i-1][1] = {A[i-1][1]}, A[i][1] = {A[i][0]}")
        if A[i-1][1] < A[i][0]:
            if maxint < A[i-1][1] - start:
                maxint = A[i-1][1] - start
            start = A[i][0]
        elif  A[i][1] > A[i-1][1]:
           A[i][1] = A[i][1]
        else:
           A[i][1] = A[i-1][1]
        # print(f"A[i][1] = {A[i][1]}")
    if maxint < A[i][0] - A[i][1]:
       maxint = A[i][0] - A[i][1]
    return maxint
 
ans = -1
N, A = InputData()
ans = Solve()
print(ans)
