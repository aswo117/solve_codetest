/*
* https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
* https://github.com/aswo117/solve_codetest/new/main/Programmers/DFS_BFS
* 
* 문제 풀이)
*  모든 경우의 수 를 구하는 문제니 BFS 로 풀이
*/

#include <iostream>
#include <algorithm>
#include <queue>

/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// float b, c;
// double d, e, f;
// char g;
// char var[256];
// long long AB;
// cin >> a;                            // int 변수 1개 입력받는 예제
// cin >> b >> c;                       // float 변수 2개 입력받는 예제 
// cin >> d >> e >> f;                  // double 변수 3개 입력받는 예제
// cin >> g;                            // char 변수 1개 입력받는 예제
// cin >> var;                          // 문자열 1개 입력받는 예제
// cin >> AB;                           // long long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// float b = 1.0, c = 2.0;               
// double d = 3.0, e = 0.0; f = 1.0;
// char g = 'b';
// char var[256] = "ABCDEFG";
// long long AB = 12345678901234567L;
// cout << a;                           // int 변수 1개 출력하는 예제
// cout << b << " " << c;               // float 변수 2개 출력하는 예제
// cout << d << " " << e << " " << f;   // double 변수 3개 출력하는 예제
// cout << g;                           // char 변수 1개 출력하는 예제
// cout << var;                         // 문자열 1개 출력하는 예제
// cout << AB;                          // long long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////

#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

int INF = 999999;
int Number[4][4] = { INF, };
int visit[4][4] = { INF, };
int result_number[17] = { 0, };
int NX[4] = { -1, 1, 0, 0 }; // 상 하 좌 우 의 X 좌표
int NY[4] = { 0, 0, -1, 1 }; // 상 하 좌 우 의 Y 좌표
int total = 0;

void BFS(int x, int y) {
	queue<pair<int, int>> q;
	visit[x][y] = 1;
	q.push(make_pair(x, y));
	int complete_number = 0;
	
	while (!q.empty()) {
		int cur_x = q.front().first;
		int cur_y = q.front().second;
		int data = Number[cur_x][cur_y];
		complete_number = complete_number * 10 + data;		
		//complete_number 가 6자리 일 경우
		int gg = complete_number / 1000000;
		if(gg >= 1 && gg < 10) {
			for (int i = 0; i < 16; i++) {
				if (result_number[i] == complete_number)
					break;
				else if (result_number[i] == 0) {
					result_number[i] = complete_number;
					total++;
					break;
				}
			}
		}

		q.pop();		
		for (int i = 0; i < 4; i++) {
			int next_x = cur_x + NX[i];
			int next_y = cur_y + NY[i];
			if (next_x >= 0 && next_x < 4 && next_y >= 0 && next_y < 4) {
				if (visit[next_x][next_y] != 1) {
					visit[next_x][next_y] = 1;
					q.push(make_pair(next_x, next_y));
				}
			}
		}
	}
}
/*
void BFS(int start) {
	queue<int> q;
	q.push(start);
	visit[start] = true;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		printf("%d ", x);
		for (int i = 0; i < a[x].size(); i++) {
			int y = a[x][i];
			if (!visit[y]) {
				q.push(y);
				visit[y] = true;
			}
		}
	}
}
*/

int main(int argc, char** argv)
{
//	ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);

	int T;
	cin >> T;

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			cin >> Number[i][j];
		}
	}

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			BFS(i, j);
		}
	}

	printf("%d", total);
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}
