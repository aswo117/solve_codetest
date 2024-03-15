#https://www.acmicpc.net/problem/2504

b = list(input().strip())
# b = list(input().split())
#inputs = list(input().strip())
stack = []


for index in b:
	if not stack:
		# print(f"[+][sung] stack is NULL index = {index}")
		stack.append(index)
	else:
		if stack[-1] == '(':
			if index == ')':
				if not stack or len(stack) == 1:
					data=2
				elif str(stack[-2]) not in '()[]':
					data = 2+stack[-2]
					stack.pop()
				else:
					data=2
				stack.pop()
				stack.append(data)
			else:
				stack.append(index)
		elif stack[-1] == '[':
			if index == ']':
				if not stack or len(stack) == 1:
					data=3
				elif str(stack[-2]) not in '()[]':
					data = 3+stack[-2]
					stack.pop()
				else:
					data=3
				stack.pop()
				stack.append(data)
			else:
				stack.append(index)
		elif type(stack[-1]) is int: # 숫자 일 경우
			if len(stack) == 1:
				stack.append(index)
			elif stack[-2] == '(':
				if index == ')':
					data = 2*stack[-1]
					stack.pop()
					stack.pop()
					if not stack:
						pass
					elif str(stack[-1]) not in '()[]':
						data = data+stack[-1]
						stack.pop()
					stack.append(data)
				else:
					stack.append(index)
			elif stack[-2] == '[':
				if index == ']':
					data = 3*stack[-1]
					stack.pop()
					stack.pop()
					if not stack:
						pass
					elif str(stack[-1]) not in '()[]':
						data = data+stack[-1]
						stack.pop()
					stack.append(data)
				else:
					stack.append(index)
	# print(stack)

if(len(stack) == 1):
	if str(stack[-1]) in '()[]':
		print(0)
	elif type(stack[-1]) is not int:
		print(0)
	else:
		print(' '.join(map(str, stack)))
else:
	print(0)
