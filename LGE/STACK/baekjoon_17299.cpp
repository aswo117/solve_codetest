// https://www.acmicpc.net/problem/17299
// 시간초과 ㅜㅠ

#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <tuple>

using namespace std;

int N;
vector <tuple<int, int, int>> v_input;
stack <tuple<int, int, int>> st_check;
vector <pair<int, int>> v_fa;
vector <pair<int, int>> v_result;

// void print_v_fa(){
// 	while(!v_fa.empty()){
// 		cout<<v_fa.back().first;
// 		cout<<v_fa.back().second<<endl;
// 		v_fa.pop_back();
// 	}
// }

// void print_v_input(){
// 	for(int i=0; i<v_input.size(); i++){
// 		cout<<get<0>(v_input[i])<<" "<<get<1>(v_input[i])<<" "<<get<2>(v_input[i])<<endl;
// 	}
// }

void print_v_result(){
	sort(v_result.begin(), v_result.end(), greater<>());
	while(!v_result.empty()){
		// cout<<v_result.back().first<<" ";
		cout<<v_result.back().second<<" ";
		v_result.pop_back();
	}
}

void make_v_fa(){
	int j;
	int data;
	cin >> N;

	for(int i = 0; i<N; i++){
		cin >> data;
		// cout<<endl<<"[+][sung] i = "<<i<<"data = "<<data<<endl;
		if(v_input.empty()){
			// cout<<"[+][sung] empty "<<endl;
			v_input.push_back(make_tuple(i, data, -1));
			v_fa.push_back(make_pair(data, 1));
		}
		else{
			v_input.push_back(make_tuple(i, data, -1));
			/* find로 안되나.. ON*N이 되버림. */
			// auto find_index = find_if(v_fa.begin(), v_fa.end(), N);	//있는지 찾기
			for(j=0; j<v_fa.size(); j++){
				if(v_fa[j].first == data){
					break;
				}
			}			
			// cout<<"[+][sung] j = "<<j<<endl;
			if(j == v_fa.size()){	//없으면
				// cout<<"[+][sung] notexsist "<<endl;
				v_fa.push_back(make_pair(data, 1));
			}
			else{
				// cout<<"[+][sung] exsist "<<endl;
				v_fa[j].second = v_fa[j].second + 1;
			}
		}
	}
}

// 여기가 의심됨.
void make_v_input(){
	for(int i=0; i<v_input.size(); i++){
		for(int j=0; j<v_fa.size(); j++){
			if(get<1>(v_input[i]) == v_fa[j].first){
				get<2>(v_input[i]) = v_fa[j].second;
			}
		}
	}
}

void Solution(){
	for(int i=0; i<v_input.size(); i++){
		// cout<<endl<<"[+][sung] i = "<<i<<"/"<<v_input.size()<<endl;
		while(1){
			if(st_check.empty() == true){
				// cout<<"[+][sung] st_check empty"<<endl;
				st_check.push(make_tuple(get<0>(v_input[i]), get<1>(v_input[i]), get<2>(v_input[i])));
				break;
			}
			else{
				if(get<2>(v_input[i]) > get<2>(st_check.top())){
					// cout<<"[+][sung] get<2>(v_input[i] : "<<get<2>(v_input[i])<<"   "<<"get<2>(st_check.top()"<<get<2>(st_check.top())<<endl;
					v_result.push_back(make_pair(get<0>(st_check.top()), get<1>(v_input[i])));
					st_check.pop();
				}
				else{
					// cout<<"[+][sung] get<2>(v_input[i] : "<<get<2>(v_input[i])<<"   "<<"get<2>(st_check.top()"<<get<2>(st_check.top())<<endl;
					st_check.push(make_tuple(get<0>(v_input[i]), get<1>(v_input[i]), get<2>(v_input[i])));
					break;
				}
			}
		}
	}
	
	while(!st_check.empty()){
		v_result.push_back(make_pair(get<0>(st_check.top()), -1));
		st_check.pop();
	}
}

int main() {
	make_v_fa();
	// print_v_fa();
	make_v_input();
	// print_v_input();
	Solution();
	print_v_result();
	return 0;
}
