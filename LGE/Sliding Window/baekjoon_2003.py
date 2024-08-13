#https://www.acmicpc.net/problem/2003

N, M = map(int, input().split())
A = list(map(int, input().split()))

sub = [0] * (N+1)
for index, val in enumerate(A):
  sub[index+1] = val+sub[index]
cnt = 0
for end in range(1, N+1):
  for start in range(end):
    if sub[end]-sub[start] == M:
      cnt += 1
print(cnt)
