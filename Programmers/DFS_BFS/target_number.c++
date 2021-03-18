#include <string>
#include <queue>
#include <vector>
#include <iostream>

using namespace std;

/* sudo
* BFS 를 이용해본다.
* 입력값은 각각 + 혹은 - 두번의 경우의 수를 지니며, 
* 이는 초기값에도 적용된다.
* Depth Search 를 하다가 number의 size만큼 내려가면 해당 값을 result와 비교하여 target과 result가 같을 경우 count 를 ++해준다.
* 결국 최종 return 값은 count 가 된다.
*/

int solution(vector<int> numbers, int target) {
	int result1 = 0;
	int result2 = 0;
	int answer = 0;
	queue<int>q;
	int k = 0;

	for(int i=0; i<2; i++){
		if(i == 0)
			q.push(numbers.front());							// 첫번째 숫자를 넣어줌 ( 양수 )
		else
			q.push(-numbers.front());							// 첫번째 숫자를 넣어줌 ( 양수 )

		while (1) {							// vetor의 전체 크기 -1
			int q_size = q.size();		
			for (int i = 0; i < q_size; i++) {			// q에 있은 front data에 numbers의 next data를 + - 하고 넣어줌.
				q.push(q.front() + numbers[k + 1]);
				q.push(q.front() - numbers[k + 1]);
				q.pop();									// 처리가 된 q는 뺴줌.			
			}
			k++;
			if (numbers.size() -1 == k)
				break;
		}
	
		int result_size = q.size();
		for(int i=0; i< result_size; i++){						//q의 사이즈만큼 
			if (q.front() == target){						// 숫자가 target이랑 같으면
				q.pop();									// 꺼내고
				answer++;									// 일치하는 answer 숫자를 늘려줌
			}
			else
			{
				q.pop();									// 아니면 그냥 pop
			}
		}
		k = 0;
	}
	
	return answer;
}

int main(){
	vector<int> numbers = { 1, 2, 2, 3, 4, 5, 7, 1 };
	int target = 3;
	cout << solution(numbers, target) << endl;
}
