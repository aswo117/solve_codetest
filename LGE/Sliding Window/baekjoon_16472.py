#https://www.acmicpc.net/problem/16472 (build err)

import sys

N = int(sys.stdin.readline())
input_data = list(sys.stdin.readline().strip())

start, end = 0, 1
cur_alpha = []
cur_alpha.appned(input_data[0])
max_count = 0

while start < len(input_data) and end < len(input_data):
	if cur_alpha == input_data[end]:
		end = end+1
		cur_alpha.append(input_data[end])
	else:
		if len(cur_alpha) < N:
			end = end+1
			cur_alpha.append(input_data[end])
		else:
			if max_count < len(cur_alpha):
				max_count = len(cur_alpha)
			start = start+1
			end = start+1
			cur_alpha = cur_alpha = input_data[start]

print(max_count)

