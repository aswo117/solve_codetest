import sys
import math
from collections import deque

N = int(input())

data_list = list()
for i in range(N):
	data_list.append(int(input()))

max_value = data_list[-1]
# print(f"max_value = {max_value}")
count = 1

while(data_list):
	if max_value >= data_list[-1]:
		data_list.pop()
	else:
		max_value = data_list[-1]
		# print(f"data_list[-1] = {data_list[-1]}")
		count = count + 1
		data_list.pop()

print(count)
		
