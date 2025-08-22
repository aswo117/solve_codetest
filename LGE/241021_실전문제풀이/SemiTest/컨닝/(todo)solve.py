'''
모든 쌍을 구하는 것이므로, 조합 문제.
전체 탐색은 N**2

정렬하고나서, 특정 값 기준으로 좌우 비교? --> 이진탐색.
잘 모르겠음. .왜 이진탐색 어케할지.. 차라리 슬라이딩윈도우(두산C)방법으로 나중에 다시 해보자.
'''
import sys
import bisect
 
def Bs_Low(s, e, d):
    sol = e
    while s<=e:
        m = (s+e)//2
        if list_file[m] >= d:
            sol, e = m, m-1
        else:
            s = m+1
             
    return sol
         

def Solve1():
    list_file.sort()
    cnt = 0
    for i in range(1, N):
       cnt += i - Bs_Low(0, i, list_file[i] * 0.9) # 내 index
    return cnt
    # return sum(i - Bs_Low(0, i, list_file[i] * 0.9) for i in range(1, N))

def Solve2():
    list_file.sort()
   #배열, 기준값, start, end (start와 end를 지정 안하면 전체 구간을 함.)
    return sum(i - bisect.bisect_left(list_file, list_file[i]*0.9, 0, i+1) for i in range(1, N))

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_file = list(map(int, readl().split()))
    return N, list_file


sol = -1
# 입력받는 부분
N, list_file = Input_Data()
 
# 여기서부터 작성
##sol = Solve1()
sol = Solve2()
 
# 출력하는 부분
print(sol)
