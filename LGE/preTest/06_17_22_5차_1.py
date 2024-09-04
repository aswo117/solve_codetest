# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#비교하는 부분이 밖이 되어야 한다

import sys
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = list(map(int,readl().split()))
    return N, num
 
 
def Quick_Sort(s, e):
    # 해당 함수의 내용에 비교/Swap 횟수를 Count 하는 내용 추가하기
    global cnt_comp,cnt_swap
    if s>=e:
      # cnt_comp = cnt_comp + 1
      return
    T,P = s,e
    for L in range(s,e):
        cnt_comp = cnt_comp + 1
        if num[L] < num[P]:
            if T != L:
                num[L],num[T] = num[T],num[L]
                cnt_swap = cnt_swap + 1
            T+=1
    if T != P:
        num[P],num[T] = num[T],num[P]
        cnt_swap = cnt_swap + 1
    Quick_Sort(s, T-1)
    Quick_Sort(T+1, e)
 
# 입력 함수
N, num = Input_Data()
 
cnt_comp,cnt_swap = 0,0
Quick_Sort(0, N-1)
 
# 출력
print(cnt_comp, cnt_swap)
print(*num)
