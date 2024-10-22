'''
greedy 문제
https://life318.tistory.com/214 참고하여 풀었음..
왜 그런지 아직도 모르겠지만
전체를 계산한 후에 나머지것들을 뺴줘서 문제를 해결
아래부터 해도 되지 않았을까.. 해보지 않았지만 뭐 무튼 이렇게 품

#총합(2679) 에서 13원 빼면 2666원
#500원 4개 2000천원 = 666원
#100원 5개 500원    = 166원
#50원  2개 100원    = 66원
#10원  6개 60원     = 6원
#5원   1개 5원      = 1원
#1원   1개 1원      = 0원
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	W = int(readl())
	cnt = list(map(int,readl().split()))
	return W, cnt


sol, sol_cnt = -1, [0] * 6
W, cnt = Input_Data()

# 여기서부터 부분
# print(W, cnt)
#cnt : 500, 100, 50, 10, 5, 1

coin_list = [500, 100, 50, 10, 5, 1]
cost_list = [cnt[0]*500, cnt[1]*100, cnt[2]*50, cnt[3]*10, cnt[4]*5, cnt[5]*1]
use_cnt = []
use_coin_count = 0
total_cost = sum(cost_list)
remain_cost = total_cost - W

# print(f"cnt = {cnt}")

for i in range(6):
	if remain_cost - cost_list[i] < 0:
		temp_count = 0
		for j in range(cnt[i]):
			if remain_cost - coin_list[i] < 0:
				use_cnt.append(temp_count)
				break
			else:
				remain_cost = remain_cost - coin_list[i]
				# print(f"i, remain_cost = {i}, {remain_cost}")
				temp_count = temp_count + 1
				use_coin_count =  use_coin_count + 1
								
	else:
		remain_cost = remain_cost - cost_list[i]
		use_cnt.append(cnt[i])
		use_coin_count = use_coin_count + cnt[i]
# 	print(f"i, remain_cost = {i}, {remain_cost}")
# 	print(f"use_coin_count = {use_coin_count}")
	
		
# print(f"use_cnt = {use_cnt}")	
# print(f"use_coin_count = {use_coin_count}")
# print(f"sum  = {sum(cnt)}")

for i in range(6):
	sol_cnt[i] = cnt[i] - use_cnt[i]

sol = sum(cnt)- use_coin_count

# 출력하는 부분
print(sol)
print(*sol_cnt)


# lamda sorting 참고
# index_list = []
# for i in range(len(cnt)):
# 	index_list.append(i)
# index_list.sort(key=lambda x:cnt[x])
# index_list.reverse()
# print(index_list)
