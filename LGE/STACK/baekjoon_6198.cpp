//https://www.acmicpc.net/problem/6198

#include <iostream>
#include <stack>
using namespace std;

int N;//건물 수
int H[80010];//건물 높이
long long ans = 0;

stack<int> st;//stack 선언

void Input_Data(void){
	int Floor;//입력받을 층 수
	cin >> N;
	for (int i = 0; i < N; i++){
		// cin >> H[i];
		cin >> Floor;
		if(st.empty() == true){
			// cout<<"empty"<<endl;
			st.push(Floor);
		}
		else{
			while(1){
				if(st.empty() == true){
					// cout<<"empty"<<endl;
					st.push(Floor);
					break;
				}
				else if(st.top() > Floor){
					ans = ans+st.size();
					st.push(Floor);
					// cout<<"[+][sung] push"<<endl<<endl;
					break;
				}
				else{
					st.pop();
					// cout<<"[+][sung] pop"<<endl<<endl;
				}
			}
		}
		// cout<<"[+][sung] ans : "<<ans<<endl;
	}
}

int main(){
	Input_Data();		//	입력 함수	
	cout << ans << endl;	//	정답 출력
	return 0;
}
