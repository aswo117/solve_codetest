import sys
from collections import deque
import math

input = sys.stdin.readline

#N : 이물질의 개수
#K : 최대 가동 횟수
N, K = map(int, input().split())
#data_list : 이물질 List
data_list = list()

data_list.append(int(0))
for i in range(N):
	data_list.append(int(input()))
data_list.sort()
# print(N, K, data_list)
# 답은 출력값이다. 출력값이 기준이어야 함.

S = 0
E = 1000000000 #이물질의 최대값 = 배열의 최대값

max_mid = 0
def check(m):
	product_count = 0 #장비 설치 개수
	start_point = 0
	if m > data_list[-1]: #입력받은 이물질 값 중 가장 큰 값보다 크면 할 필요 없다.
		return 0
	else:
		for idx, data in enumerate(data_list):
			if m*2 - (data_list[idx] - data_list[start_point]) <= 0: #출력값의 2배(양쪽으로 봐야 함으로)가 슈래기를 다 볼수 있을때 까지 이동
				start_point = idx #여기서 부터 슈레기 봐야함
				product_count = product_count+1
	
	return product_count	
	
while S<=E:
	mid = (S+E)//2
	
	total = check(mid) #mid 는 출력값
	if total == 0: #입력 값이 쓸모없는 값이 들어왔을경우
		E = mid - 1
	elif total >= K: #가동횟수 K 보다 큰 값이 들어오면 줄어도 되니
		S = mid+1
		if max_mid < mid:
			max_mid = mid
	else:
		E = mid-1

print(max_mid) #첫번째 mid 값이 가장 작은 출력값이므로, 
