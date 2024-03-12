#https://www.acmicpc.net/problem/17298
#반례찾아야됨.

N = int(input())
b = list(map(int, input().split()))
stack = []
ans = [-1]*N

# print(f"[+][sung]")
# print(f"[+][sung] N = {N}, b = {b} stack = {stack} ans = {ans}")

for index in range(N):
	# print(f"[+][sung] index = {index}, N = {N}, stack = {stack}")
	while(1):
		if not stack:
			# print(f"[+][sung] stack is NULL")
			stack.append(index)
			break;
		elif b[index] > b[stack[-1]]:
			ans[stack[-1]] = b[index]
			stack.pop()
		else:
			stack.append(index)
			break;
			
# for index in range(N):
print(f"{ans}")
