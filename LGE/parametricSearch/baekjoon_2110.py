import sys
from collections import deque

input = sys.stdin.readline

# print(f"[+][sung] ")

N, C = map(int, input().split())
data_list = list()
dist_list = list()
solve = 0

for i in range(N):
	data_list.append(int(input()))
data_list.sort()
# print(N, C, data_list)
for j in range(N-1):
	dist_list.append((data_list[j]-data_list[j+1])*-1)

def check(m):#공유기의 거리가 m
	temp = 0
	if data_list[-1] < m: #공유기의 처리 거리가 전체 집거리보다 클 경우 일단 거르고
		return 0
	
	print(f"[+][sung] dist_list = {dist_list}")
	remain_dist = m
	print(f"[+][sung] remain_dist = {remain_dist}")
	while 1: #1번 집을 시작으로 공유기의 처리 거리가 끝날때 까지 반복
		for i in dist_list: #각 집마다의 거리를 빼주기위한 배열
			print(f"[+][sung] {remain_dist} = {remain_dist} - {i}")
			remain_dist = remain_dist - i #남은 거리를 뽑아서			
			if remain_dist <= 0: #더이상 못 뽑으면
				return temp
			else: #뽑을 수 있으면 공유기 개수 추가 한 뒤 다음 집까지 간다.
				temp = temp+1

S = 0
E = 1000000000

while S<=E:
	mid = (S+E)//2
	total = check(mid) #return 값은 공유기 설치 숫자
	
	print(f"[+][sung] total = {total}")
	if total >= C: #같으면 최적값임.
		solve = mid
	elif total > C:
		S = mid+1
	else:
		E = mid-1
	

	
