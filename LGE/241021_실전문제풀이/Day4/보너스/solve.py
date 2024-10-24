#해설
'''
#BFS - 가중치가 동일한지 다른지, 경우의수가 어떻게 되는지(상하좌우, 대각선)
#DFS - 경우의 수. 순열(아이템을 중복으로 사용할 수 있냐? 중복순열, 아니면 순열), 조합(중복조합, 조합)
       중복순열 : 경우의수가 작아야되고, Depth도 작아야됨. 경우의 수의 복잡도는 중복순열>순열>중복조합>조합
이 문제는 순열 문제다. = Factorial
순열 : permutations << 파이썬 api : 근데 10Fac이면 메모리 초과임.(128MB 이상 불가) - 가급적 쓰지말자. 메모리가 너무 소모됨.
from itertools import permutations

'''

import sys
from itertools import permutations

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	relation = [list(map(int, readl().split())) for i in range(M)]	
	bonus = list(map(int, readl().split()))
	return N, M, relation, bonus


sol = []
# 입력받는 부분
#N은 직원의 수 M은 상하관계
N, M, relation, bonus = Input_Data()

# 여기서부터 작성
#방법 1 permutations 사용
#10 팩토리알 하면 time out
#첫번째는 항상 사장이니 9 팩으로 가능
# def isPossilbe(ans):
# 	for s, e in relation: #관계도에서
# 		if ans[s] <= ans[e] : return False #상급자보다 하급자가 같거나 크면
# 	return True
# def solve():
# 	ans = [0] * N+1 # 1~0번까지 담아야 되니.
# 	bonus.sort()#소팅해서 마지막에 큰거를 담기 위함.
# 	ans[1] = bonus[-1] #사장꺼 가장 큰거
# 	for c in permutations(bonus[:-1]): #마지막꺼는 사장꺼니 필요없음
# 		ans[2:] = c #일단 답을 다 담고
# 		if isPossible(ans) : break #검증을 하면 됨.
# 	return ans

#방법2 DFS 활용
#순열, 다중루프
def isPossilbe(n, c, ans, info):
	for i in range(1, n):
		if info[n][i] and c <= ans[i]: #내가 상급자고, 하급자가 나보다 돈을 많이 받거나 같으면
			return False
		if info[i][n] and c >= ans[i]: #내가 하급자고, 상급자보다 더 많이 받으면
			return False
	return True
def dfs(n, ans, used, info):
	#종료조건
	if n>N: #직원에게 다 지불했으면
		return True
	for i in range(N):
		if used[i] == True: #이미 지불 했으면
			continue
		if not isPossilbe(n, bonus[i], ans, info): #지불하면 안되면
			continue
		used[i] = True
		ans[n] = bonus[i]
		if dfs(n+1, ans, used, info) == True: #다 지불했으면 빠져나감, 
			return True
		used[i] = False
		ans[n] = 0
	
	return False

def solve():
	ans = [0] * (N+1)  # 1번부터 사용하기위해 +1
	used = [False] * N # bounus 사용 여부 확인
	info = [[False]*(N+1)for _ in range(N+1)] #관계도 필요

	#사장한테 가장 큰 금액 주기
	ans[1] = max(bonus)
	used[bonus.index(ans[1])] = True
	
	#관계도 업데이트
	for s, e in relation:
		info[s][e] = True #상급자 하급자 관계 업데이트
	
	dfs(2, ans, used, info)
	return ans
	
# sol = solve()
sol = solve()

# 출력하는 부분
print(*sol[1:])




