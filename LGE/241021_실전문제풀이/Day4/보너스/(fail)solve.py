#나중에 질문하려고 남겨둠

#그래프로 풀려고 시도함.
#는 DFS래.. 
import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	relation = [list(map(int, readl().split())) for i in range(M)]	
	bonus = list(map(int, readl().split()))
	return N, M, relation, bonus

sol = []
# 입력받는 부분
N, M, relation, bonus = Input_Data()
print(f"N, M, relation, bonus = {N, M, relation, bonus}")
# 여기서부터 작성

data_list = [[] for i in range(N+1)]
data_cnt_list = []

#인접 리스트 생성
for i in range(M):
	s, e = relation[i][0], relation[i][1]
	data_list[s].append(e)

print(f"data_list = {data_list}")
#부하의 부하직원까지 넣자.
for i in range(M):
	#i 는 0 ~ M 까지 들어와
	#ex. 2 4 5 의 길이만큼 for문 돌아감.
	for j in range(len(data_list[i])):
		# i = 1이야
		# j = 3이 될꺼야.
		#2 4 5에 해당하는 부하 직원들을 출력해보자. ex. 3 4(2) [] []
		#data_list[i] 는 2 4 5가 될꺼고, 여기에 차례로 2 4 5 를 하나씩 뽑아서 data_list에 확인
		temp_list1 = data_list[i]
		temp_list2 = data_list[data_list[i][j]]
		data_list[i] = list(set(temp_list1+temp_list2))

#부하가 많은 순서대로 bonus를 주면 되지 않을까? -> 안될꺼같아..
#그래프가 아니라 DFS일꺼같아.->아닐꺼같아.
#그러면 인접리스트 + 그 부하의 부하까지 개수를 더하면 되지 않을까? 
# print(data_list)

#부하의 개수 list를 생성하자.
for i in range(1, M):
	data_cnt_list.append(len(data_list[i]))
print(data_cnt_list)

#data_cnt_list 오름차순 순으로 bonus를 소팅해주자.
#는 안됨. 어케해야될까.
print(bonus)
bonus.sort(key=lambda x:data_cnt_list[x])
print(bonus)

# # 출력하는 부분
# print(*sol[1:])

# a = [2, 3, 1, 7]
# index_list = [0, 1, 2, 3]
# index_list.sort(key=lambda x:a[x])
# print(a)
