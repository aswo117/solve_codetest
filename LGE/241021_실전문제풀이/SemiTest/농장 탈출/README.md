- 문제 설명
```
소들은 농부 존의 농장을 탈출하는 대담한 계획을 세웠다. 그들은 작은 고무 보트를 구했고
한 밤중에 농장 경계에 흐르는 강을 보트를 타고 건너려는 계획이다.
그 계획은 완벽해 보였다. 작은 고무 보트가 소들의 무게를 견디지 못한다는 사실을 알기 전까지는…
 
N마리의 소(1≤N≤20)들의 무게는 각각 W_1, …, W_N이다. 보트가 침몰하지 않을 만큼 가벼운 소들을 선별해야 한다.
불행하게도, 소들은 산수를 못하기로 유명하다.
10진법을 사용하는 소들은 소들의 무게를 더하다가 자리올림이 발생하는 경우
그 소는 보트를 사용하기에는 너무 무거운 소라고 판단한다.
자리올림이 발생하지 않고 더할 수 있는 무게가 보트를 사용할 수 있는 가벼운 무게이다.
 
당신이 할 일은 소들을 도와서 보트를 탈 수 있는 소들의 최대 수를 구하는 것이다.
즉, 소들의 무게들을 모두 더했을 때 자리올림이 발생하지 않게 하는 소들의 최대 수를 구하는 것이다.
```
- 입출력 Template이 필요한 경우 Python 제출은 다음 코드를 복사하여 코드를 작성하시오.
```
import sys

 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	weight = [int(readl()) for _ in range(N)]
	return N, weight
 

sol = -1
# 입력받는 부분
N, weight = Input_Data()
 
# 여기서부터 작성

 
# 출력하는 부분
print(sol)
```
- 입력 설명
```
첫 줄에 소들의 수 N(1≤N≤20)이 주어진다.
두 번째 줄부터 N 줄에 걸쳐 각 소의 무게(W_i)가 입력된다. (정수, 1≤W_i≤100,000,000)
```
- 출력 설명
```
무게를 모두 더했을 때 어떤 자리에서도 자리올림이 발생하지 않는 소들의 최대 수를 출력하라.
```
- 입력 예시
```
5
522
6
84
7311
19
```
- 출력 예시
```
3
```
- 힌트
![image](https://github.com/user-attachments/assets/ea8f82ac-070f-4287-9da2-f99e67cd56fd)

