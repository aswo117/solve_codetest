#Stack 이용
#어거지로 맞춤..

import sys
from collections import deque
 
def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    num = readl().strip()
    return N, K, num
 
sol = -1
# 입력받는 부분
N, K, num = Input_Data()

stack = []
# 여기서부터 작성
# print(f"N, K, num = {N, K, num}")

for i in range(N):
	# print(f"num[i] = {num[i]}")
	# print(f"K = {K}")
	if K == 0:
		for i in range(i, N):
			stack.append(num[i])
		break
	while 1:
		if not stack:
			stack.append(num[i])
			break
		if len(stack) == N-K+1:
			stack.pop()
			break
		else:
			if stack[-1] < num[i]:
				stack.pop()
				K = K-1
				if K == 0:
					stack.append(num[i])
					break
			else:
				stack.append(num[i])
				break
				
	# print(f"stack = {stack}")
# print(stack)
print(''.join(map(str, stack)))
