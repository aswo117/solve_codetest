//https://www.acmicpc.net/problem/17298

#include <iostream>
#include <stack>
#include <algorithm>
#include <vector>
using namespace std;

int N;
stack<pair<int, int>> st_input;
vector<pair<int, int>> v_output;

// bool compare(int i, int j){
// 	return j<i;
// }

void print_data(){
	sort(v_output.begin(), v_output.end(), greater<>());
	while(!v_output.empty()){
		// cout<<v_output.back().first<<" ";
		cout<<v_output.back().second<<" ";
		v_output.pop_back();
	}
}

void Solution(void){
	int data;
	cin >> N;
	// cout<<"[+][sung] : "<<endl
	// cout<<endl<<"[+][sung] N : "<<N<<endl;
		
	for (int i = 0; i < N; i++){
		cin >> data;
		// cout<<endl<<"[+][sung] i : "<<i<<endl;
		// cout<<"[+][sung] data : "<<data<<endl;

		while(1){
			if(st_input.empty() == true){
				st_input.push(make_pair(i, data));
				// cout<<"[+][sung] empty push input data : "<<st_input.top().second<<endl;
				break;
			}
			else{
				// cout<<"[+][sung] top : "<<st_input.top().second<<endl;
				if(data > st_input.top().second){
					v_output.push_back(make_pair(st_input.top().first, data));
					// cout<<"[+][sung] push output data : "<<st_input.top().second<<endl;
					st_input.pop();
				}
				else{
					st_input.push(make_pair(i, data));
					// cout<<"[+][sung] push input data : "<<st_input.top().second<<endl;
					break;
				}
			}
		}
	}
	
	while(!st_input.empty()){
		v_output.push_back(make_pair(st_input.top().first, -1));
		st_input.pop();
	}
}

int main(){
	Solution();
	print_data();
	return 0;
}
