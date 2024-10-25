import sys
 
def isPossible(a, b):
    while a and b:
        if a%10 + b%10 >= 10: return False
        a //= 10
        b //= 10
    return True
 
def DFS_M(s, sum_weight, cnt): #시작인덱스, 태운 무게 합, 태운 마리수
    global sol
    if sol >= cnt + (N-s): return #이전 답보다 좋은 답을 구할 가능성 없음(현재까지 태운소+남은소 전부)
    if sol < cnt: sol = cnt #답 갱신
    for i in range(s, N):#조합
        if not isPossible(sum_weight, weight[i]): continue
        DFS_M(i+1, sum_weight + weight[i], cnt + 1)
 
def DFS_B(n, sum_weight, cnt): #인덱스, 태운 무게 합, 태운 마리수
    global sol
    if sol >= cnt + (N-n): return #이전 답보다 좋은 답을 구할 가능성 없음(현재까지 태운소+남은소 전부)
 
    if sol < cnt: sol = cnt #답 갱신
 
    if n >= N: return #종료조건
 
    if isPossible(sum_weight, weight[n]):#태우는 경우(조건이 만족해야 가능)
        DFS_B(n+1, sum_weight + weight[n], cnt + 1)
         
    DFS_B(n+1, sum_weight, cnt) #안 태우는 경우(조건 상관 없음)
  
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight
  
 
sol = -1
# 입력받는 부분
N, weight = Input_Data()
  
# 여기서부터 작성
##DFS_B(0, 0, 0)
DFS_M(0, 0, 0)
  
# 출력하는 부분
print(sol)
