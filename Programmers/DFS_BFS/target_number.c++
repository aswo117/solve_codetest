#include <string>
#include <vector>
#include <iostream>

using namespace std;

int visited[20];

/* sudo
* DFS 를 이용해본다.
* 입력값은 각각 + 혹은 - 두번의 경우의 수를 지니며, 
* 이는 초기값에도 적용된다.
* Depth Search 를 하다가 number의 size만큼 내려가면 해당 값을 result와 비교하여 target과 result가 같을 경우 count 를 ++해준다.
* 결국 최종 return 값은 count 가 된다.
*/

int DFS(int count, int result, vector<int> numbers, int target) {
	while (count != numbers.size()) {

	}
}
int solution(vector<int> numbers, int target) {
	return DFS(0, 0, numbers, target);
}

int main(){
	vector<int> numbers = { 1, 1, 1, 1, 1 };
	int target = 3;
	cout << solution(numbers, target) << endl;
}

/*
void DFS(int x) {
	if (visit[x]) return;
	visit[x] = true;
	printf("%d ", x);
	for (int i = 0; i < a[x].size(); i++) {
		int y = a[x][i];
		DFS(y);	// 스택에 넣는다고 생각하면 됨.
	}
}
*/
