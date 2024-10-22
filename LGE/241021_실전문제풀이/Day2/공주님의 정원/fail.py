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

#월 일 정보를 압축해서 저장. ex. 01/01 = 101, 03/31 = 331
info_list = []
for i in range(N):
	info_list.append([info[i][0]*100+info[i][1], info[i][2]*100+info[i][3]])
# print(info_list)
info_list.sort()

#cnt 선택한 개수, idx 인덱스, end 끝값
cnt, idx, end = 0, 0, 301#최초의 끝나는 날짜
flag = False
while 1:
	#초기값 101~301에서 피는 꽃 중에 가장 늦게 피는 꽃
	if flag == True:
		break

	maxv = 0
	while idx<N and info_list[i][0]<=end: #0은 피는날, #1은 지는날 즉 초기값을 예로들면 301이므로 301보다 작은 피는날이 들어옴
		maxv = max(maxv, info_list[i][1]) #1은 지는날. 이때 지는날이 가장 큰 값을 maxv에 저장
		idx += 1 #다음 list로 이동
	if maxv <= end: #이렇게 찾은 maxv값이 end즉 301(초기값을 예로들어)보다 작은 값이면 301보다 작기 떄문에 
		end = 0 #실패
		flag = True
		break
	else: #안에 들어오면
		cnt += 1 #list에 들어온 것이니까 cnt를 올려줌
		if maxv > 1130 : #근데 이때 maxv가 1130보다 크면 끝내도 되니
			end = maxv #끝값에 최대값을 넣고 종료
			break

print(cnt)


# def solve1():
#     flower_info = [[sm*100+sd, em*100+ed] for sm,sd,em,ed in info]
#     flower_info.sort()
 
#     cnt, i, e = 0, 0, 301
#     while True:
#         maxv = 0
#         while i<N and flower_info[i][0]<=e:
#             maxv = max(maxv, flower_info[i][1])
#             i += 1
#         if maxv <= e: return 0 #실패
 
#         cnt += 1
#         if maxv > 1130 : return cnt #성공
#         e = maxv

#정렬 좌측 List 기준으로 (시작 일)
#tip 월*100, + 일로 한다음 비교해.
# info.sort() # 월로만 비교했음. 일로도 비교하는거 추가하자. lamda 이용해도 될듯?

#0, 1이 좌측임
#2, 3이 우측임


# #1. 처음 시작 조건은 무족건 3월이 포함되어야 함.
# #2. 3월 1일 이 포함된 첫 시작값이 들어오면, 이후 들어오는 값은 이전값과 연결되어야 함.
# #3. 연결된 값이 들어오되, 끝 지점이 더 크면 그걸로 바꿔줌
# #4. 이때 11월 30일이 넘어가면 끝냄


#fail_1

# info.sort(key=lambda x:(x[0], x[1]))

# result = []
# for i in range(N):
# 	if info[i][0] < 3 or (info[i][0] == 3 and info[i][1] == 1): # 3월보다 작거나 3월 1일이면
# 		if not result: #처음 들어온 값이면 Stack에 넣기
# 			result.append(info[i])
# 		else:
# 			# print(f"result[2], info[i][2], result[3], info[i][3] = {result[2], info[i][2], result[3], info[i][3]}")
# 			# print(info[i][2])
# 			if result[0][2] < info[i][2] or (result[0][2] == info[i][2] and result[0][3] < info[i][3]): #첫 값을 정하는데, 이미 들어와 있는 값보다 끝나는 값이 크면 바꿔
# 				result.pop()
# 				result.append(info[i])	
	#3월보다 큰 값들이 들어와서 뒤에 붙여줘야 되는 값이 들어옴, 
	#이미 들어온 값의 top의 3, 4번쨰(2, 3) 와 들어온 값의 1, 2 번쨰(0, 1) 비교
	#이미 들어온 값의 top의 1번째(월)이 들어올 값의 3번째(월)보다 커야 안으로 들어옴. 같을 경우 일(2번쨰 vs 4번째)이 더 커야함.
# 	elif info[i][0] < result[-1][2] or (info[i][0] == result[-1][2] and info[i][1] < result[-1][3]): 
# 		# print(f"len = {len(result)}")
# 		while(1):
# 			#들어올 자격은 있는데 이 전값과 비교해서 안으로 들어올 수 있고
# 			if not (len(result) == 1) and (info[i][0] < result[-2][2] or (info[i][0] == result[-2][2] and info[i][1] < result[-2][3])):
# 				#현제 값보다 범위가 넓으면 뽑아
# 				if info[i][2] > result[-1][2] or (info[i][2] == result[-1][2] and info[i][3] > result[-1][3]):
# 					result.pop()
# 					result.append(info[i])
# 				else:
# 					break
# 			else:	
# 				result.append(info[i])
# 				break
# # print(f"result = {result}")

# if result[-1][2] > 11 or (result[-1][2] == 11 and result[-1][3] >= 30):
# 	print(len(result))
# else:
# 	print(0)
