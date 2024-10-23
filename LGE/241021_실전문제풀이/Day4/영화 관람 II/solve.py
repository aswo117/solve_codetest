'''
그.. 그 두산책임님 유형중 하나 문제
첫번째 정렬하냐 두번째 정렬하냐 기간을 정렬하냐를 정해야됨
1. 그래프를 그려서 고려할것.
2. 반례를 생각해볼것.

그리고 둘다 정렬하면 대부분 다 좋음 lambda 를 활용하자
ex)
info.sort(key=lambda x:(x[1], x[0)) # info[1]로 정렬하고 같으면 info[0]으로 정렬
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	info = [list(map(int, readl().split())) for _ in range(N)]
	return N, info


sol = -1
# 입력받는 부분
N, info = Input_Data()
 # 여기서부터 작성

# print(f"N, info = {N, info}")
# 끝 시간 기준으로 정렬
# 정렬 3가지 - 시작시간, 끝시간, 상영시간
# 시작시간이 짧고 길면 오랫동안 상영하면 답없어짐. 종료시간이 잛아야됨.
# 시작시간 반례
'''
10
7 12
20 23
19 20
2 7
6 8
11 14
13 16
1 22
4 8
15 19
'''
info.sort(key=lambda x:(x[1], x[0]))
# info.sort()
# print(f"N, info = {N, info}")

start_time = 0
end_time = 0
stack = []

for i in range(N):
	#비어있으면, 2시간 이상 영화를 골라 넣어.
	if not stack:
		if info[i][1] - info[i][0] >= 2:
			stack.append(info[i])	
	else:
		#1. 현제 보고 잇는 영화의 끝시간(stack[-1][1]) 보다 들어올 영화의 시작시간(info[i][0])이 크거나 같아야됨.
		if stack[-1][1] <= info[i][0]:
			#2. 들어올 영화의 총 시간이 2시간 이상이어야 됨.
			if info[i][1] - info[i][0] >= 2:
				stack.append(info[i])
		
# 출력하는 부분 
sol = len(stack)
print(sol)
