#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

int N;//건물 수

stack<pair<int, int>> st_input;
queue<int> queue_output;

void print_result(void){
	while(!queue_output.empty()){
		cout<<queue_output.front()<<" ";
		queue_output.pop();
	}
}

void Solution(void){
	cin >> N;
	// cout<<"[+][sung] N : "<<N<<endl;
	for (int i = 0; i < N; i++){
		int data;
		cin >> data;
		while(1){
			if(st_input.empty() == true){
				st_input.push(make_pair(i+1, data));
				queue_output.push(0);
				break;
			}
			else{
				// cout<<"st_input.top().first : "<<st_input.top().first<<endl;
				// cout<<"st_input.top().second : "<<st_input.top().second<<endl;
				if(data < st_input.top().second){
					queue_output.push(st_input.top().first);
					st_input.push(make_pair(i+1, data));
					break;
				}
				else{
					st_input.pop();
				}
			}
		}
	}
}

int main(){
	Solution();
	print_result();
	return 0;
}
