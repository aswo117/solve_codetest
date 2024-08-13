import sys

input_data = []

N, K = map(int, input().split())
# N, K = map(int, sys.stdin.readline().split())
feed_list = [0]*1000001
feed_max = 0
temp_ans = 0
ans = 0
window_size = K*2+1

for i in range(N):
	value, index = map(int, sys.stdin.readline().split())
	# input_data.append((value, index))
	feed_list[index] = value
	if index > feed_max:
		feed_max = index	
		
# print(feed_list[:feed_max])
temp_ans = sum(feed_list[:window_size])
ans = temp_ans

for i in range(window_size, feed_max+1):
	# print(feed_list[i+1])
	# print(f"{i+1-window_size} - {feed_list[i+1-window_size]}")
	temp_ans = temp_ans+feed_list[i] - feed_list[i-window_size]
	# print(f" i = {i} temp_ans = {temp_ans}")
	if temp_ans > ans :
		ans = temp_ans
		
print(ans)
