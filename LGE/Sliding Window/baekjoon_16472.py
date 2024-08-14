#https://www.acmicpc.net/problem/16472 (70% fail)

import sys

N = int(sys.stdin.readline())
input_data = list(sys.stdin.readline().strip())

start, end = 0, 0
cur_alpha = []
cur_alpha.append(input_data[0])
max_count = 0
check_count = 0

while start < len(input_data)-1 and end < len(input_data)-1:
	if N > check_count and end <= len(input_data):
		end = end+1
		if input_data[end] not in cur_alpha:
			check_count = check_count + 1
		cur_alpha.append(input_data[end])
	else:
		if max_count < len(cur_alpha)-1:
			max_count = len(cur_alpha)-1
		start = start+1
		end = start
		check_count = 0
		cur_alpha = [input_data[start]]

print(max_count)



