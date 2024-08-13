#https://www.acmicpc.net/problem/2230

import sys

N, M = map(int, input().split())
input_data = []
ans = 2000000001
for i in range(N):
	input_data.append(int(sys.stdin.readline()))
input_data.sort()

start, end = 0, 0

while start<=end and end < N:
	if input_data[end]-input_data[start] < M:
		end = end+1
	else:
			if ans > input_data[end]-input_data[start]:
				ans = input_data[end]-input_data[start]
			
			start = start+1 

print(ans)

