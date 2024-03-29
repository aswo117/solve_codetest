N = int(input())
H = [0]*N
result = 0
stack = []

for index in range(N):
	H[index] = int(input())

for index in range(N):
	if not stack:
		stack.append(H[index])
	else:
		while(1):
			if not stack or H[index] < stack[-1]:
				result = result + len(stack)
				# print(f"result = {resWult}")
				stack.append(H[index])
				break
			else:
				stack.pop()
		
print(result)
	
# print(N, H)
