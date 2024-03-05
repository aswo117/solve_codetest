#include <iostream>
#include <stack>
#include <queue>
using namespace std;

int N;//건물 수
// int H[500000];//탑 높이
int result[500000];//탑 높이

stack<int> st_input;
queue<int> queue_output;

// void print_input(void){
// 	for(int i=N-1; i>=0; i--){
// 		cout<<"H["<<i<<"] : "<<H[i]<<endl;
// 	}
// }

void print_result(void){
	while(!queue_output.empty()){
		cout<<queue_output.front()<<" ";
		queue_output.pop();
	}
}

void Input_Data(void){
	cin >> N;
	// cout<<"[+][sung] N : "<<N<<endl;
	for (int i = 0; i < N; i++){
		int data;
		cin >> data;
		if(st_input.empty() == true){
			// cout<<"[+][sung]empty"<<endl;
			queue_output.push(0);
			st_input.push(data);
			// cout<<"0"<<endl;
		}
		else{
			if(data < st_input.top()){
				// cout<<"[+][sung] < : "<<queue_output.size()<<endl;
				queue_output.push(queue_output.size());	
				st_input.push(data);
			}
			else if(data == st_input.top()){
				// cout<<"[+][sung] == : "<<queue_output.back()<<endl;
				queue_output.push(queue_output.back());
				st_input.push(data);
			}
			else{
				// cout<<"[+][sung] > : "<<queue_output.back()<<endl;
				queue_output.push(queue_output.back());
				st_input.push(data);
			}
		}
	}
}

int main(){
	Input_Data();		//	입력 함수
	print_result();
	return 0;
}

//출력 오류
