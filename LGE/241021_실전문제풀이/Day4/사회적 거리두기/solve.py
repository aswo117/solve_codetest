#파라메틱 서치
#범위가 졸라큼
#하나의 행에서 움직임
#중간마다 잘라가면서 탐색 혹은 계산

import sys

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int,readl().split())
	intvals = [list(map(int,readl().split())) for _ in range(M)]
	return N, M, intvals


sol = -1
#입력받는 부분
N, M, intvals = Input_Data()
# print(f"N, M, intvals = {N, M, intvals}")
intvals.sort(key=lambda x:(x[0], x[1]))

# print(f"intvals = {intvals}")

# 여기서부터 작성

# cow는 0에 일단 넣고
# 최대값이 10*18승인데 이걸 파라매틱 서치(2진 서치)를 이용해서 cow + 이진 서치 오는 값에 잔디에 들어올 때 까지 탐색.

def check(m): #m 은 거리.
	cow_pos = intvals[0][0] #소는 첫 지점에서 시작 (ex. 0)
	cow_cnt = 1
	i = 0 #팬스 좌표
	#반복하는데 팬스 개수 만큼(M)
	while 1:
		# print(f"cow_cnt = {cow_cnt}")
		# print(f"cow_pos = {cow_pos}")
		# print(f"intvals[i] = {intvals[i]}")
		if cow_cnt == N: #소를 다 배치했으면
			return True
		if i >= M: #펜스 개수가 넘어가면
			return False
		if cow_pos + m >= intvals[-1][-1]: #소에 거리 더한게 마지막보다 크면 False
			return False
		# if intvals[i][0] <= cow_pos + m and cow_pos + m <=  intvals[i][1]: #현제 팬스안에 들어가면
		# 	cow_cnt = cow_cnt+1 #소 카운트 더해주기
		# 	cow_pos = cow_pos + m #소 위치를 넣어주고
		# else:#아니면 다음 팬스 첫 지점으로 카우 위치를 옮겨주고 다음 fence로 넘어가자
		# 	cow_pos = intvals[i+1][0]
		# 	cow_cnt = cow_cnt+1
		# 	i = i+1

		if cow_pos + m <= intvals[i][1] : # 강사수정 배치 가능(끝 위치보다 작으면 배치가능)
			cow_pos = (cow_pos + m) if cow_pos + m >= intvals[i][0] else intvals[i][0] #강사수정 시작위치 보다 작으면 시작위치에 배정
			cow_cnt = cow_cnt + 1
		else: # 아니면 다음 팬스 첫 지점으로 카우 위치를 옮겨주고 다음 fence로 넘어가자
			i = i + 1
		if i >= M : 
			return False
			
			
S = 0
E = 10**18 #파라매틱 서치는 E가 많이 커도됨, 평균 넣으면 속도 많이 줄어듬.
while S<=E:
	mid = (S+E)//2 #mid는 소와 소사이의 거리
	# print(f"mid = {mid}")
	if check(mid) == True: #True가 리턴 됬을때만 동작
		# print(f"True, sol = {sol}")
		sol = mid
		S = mid+1		
	else:
		E = mid-1
# 출력하는 부분
print(sol)
