#가중치가 다른 BFS
#중복방문을 허용하면 됨 - 좋은 경우에만 방문하면 됨
#map을 하나 더 만들어서 가중치를 저장함
#그래서 비교해서 좋은 경우만(같은경우 말고) 저장함
#큰 값으로 초기화 하고
 
# (1,0 ~ 0,N-1) 까지 input 그리고 (1,0 ~ N-1,0) 그리고 (N-1,0 ~ N-1,N-1) 그리고 (0,N-1 ~ N-1,N-1)의 input이 들어가고 각각의 목표치까지 최단 경로를 구하면 됨.
# --> 시간 초과됨... BFS 를 최대 400번 호출할 태니까.
#     그럼? 목적지에서 출발시켜라.
#     그 후 둘래에서 나오는 값들 중 최소값을 구해라.
#     오르막 내리막 잘 생각해라. 목적지에서 출발한다고 반대로 하면 안됨.
# 이때 goal은 r_top, c_top
 
import sys
import math
from collections import deque
 
 
def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    r_top, c_top = map(int, readl().split())
    map_mountine = [[0] + list(map(int,readl().split())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
    return N, r_top, c_top, map_mountine
 
def print_que():
    for i in range(N+2):
        print(f"{visitied[i]}")
    print("\n") 
 
sol = -1
# 입력받는 부분
N, r_top, c_top, map_mountine = Input_Data()
 
# print(f"N, r_top, c_top, map_mountine = {N, r_top, c_top, map_mountine}")
# 여기서부터 작성
 
#visitied 생성, 높은 값으로 초기화
visitied = [[math.inf for i in range(N+2)] for j in range(N+2)]
 
#Start 지점에서 출발 = r_top, c_top
q = deque()
q.append((r_top, c_top))
visitied[r_top][c_top] = 0
 
result_min = math.inf
 
while q:
    x, y = q.popleft()
    # print(f"x, y = {x, y}")
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)): #상 하 좌 우
        nx, ny= dx+x, dy+y
         
        #외각도 일단 다 저장해주자.. 이럴떈 N+1도 포함해야 되는거 아닌가..?
        if not (0<=nx<N+2) or not (0<=ny<N+2):
            continue
         
        #이동되면 나오는 값을 계산해줌 주의점은 지금 꼭대기에서 바닥으로 이동중임 이동하는 포인트가 nx, 이전값이 x임
        next_value = 0
        if map_mountine[nx][ny] > map_mountine[x][y]:
            #내려가는거야 실제론 (차이)
            next_value = map_mountine[nx][ny] - map_mountine[x][y]
        if map_mountine[nx][ny] < map_mountine[x][y]:
            #올라가는거야 실제론 (제곱)
            next_value = (map_mountine[x][y] - map_mountine[nx][ny]) ** 2
        if map_mountine[nx][ny] == map_mountine[x][y]:
            #평지(에너지 소비 0)
            next_value = 0
             
        if visitied[nx][ny] > next_value + visitied[x][y]:
            visitied[nx][ny] = next_value + visitied[x][y]
            q.append((nx, ny))
         
        # print_que()       
# 출력하는 부분
 
sol = visitied[0][0]
print(sol)
