#https://www.acmicpc.net/problem/16472 (build err)

import sys

N = int(sys.stdin.readline())
input_data = list(sys.stdin.readline().strip())

start, end = 0, 1
cur_alpha = []
cur_alpha.append(input_data[0])
max_count = 0

while start < len(input_data) and end < len(input_data):
	print(f"N = {N}")
	print(f"len(input_data) = {len(input_data)}")
	print(f"max_count = {max_count}")
	print(f"cur_alpha = {cur_alpha}")
	if N >= len(input_data):
		end = end+1
		if input_data[end] not in cur_alpha:
			cur_alpha.append(input_data[end])
	else:
		if max_count < len(cur_alpha):
			max_count = len(cur_alpha)
		start = start+1
		end = start
		print(f"input_data[start] = {input_data[start]}")
		print(type(input_data[start]))
		cur_alpha = cur_alpha[input_data[start]]

print(max_count)


