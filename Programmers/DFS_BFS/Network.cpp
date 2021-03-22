/*
* https://github.com/aswo117/solve_codetest/edit/main/Programmers/DFS_BFS/Network.cpp
* https://programmers.co.kr/learn/courses/30/lessons/43162
* 
* 분석)
* Network 숫자를 구하는 문제
* 대놓고 Union-find(Disjoint-set) 문제로 보인다.
* 
* Union-find를 다시보면 (https://m.blog.naver.com/ndb796/221230967614)
* 이론)
* 여러 개의 노드가 존재할 떄 두 개의 노드를 선택해서 현재 이 두 노드가 서로 같은 그래프에 속하는지 판단한다.
* 1. 첫번째 행은 "노드 번호", 두번째 행은 "부모 노드 번호"를 의미한다. (이때 자기자신으로 초기화한다.)
* 2. 연결되어 있다면, "일반적으로 작은 값"으로 "부모 노드 번호"를 변경한다. 이것을 "Union" 이라고 한다.
*    이때 연속된 연결점이 있다면 "재귀함수"를 이용하여 "가장 작은 값"으로 업데이트 한다.
*    ex) 1, 2, 3 이 연결되어 있다.
*        초기값은 (1, 1) (2, 2) (3, 3) 이겠지만
*        Union 작업을 하게된다면 (1, 1), (2, 1), (3, 1)이 된다.
* 3. 두 개의 노드의 부모 노드를 확인하여 같은 집합에 속하는지 확인하는 과정이 Find 과정이다.
* 
* 즉 이 두작업을 합쳐서 Union Find 라고 한다.
*/ 


#include <string>
#include <vector>
#include <iostream>

using namespace std;

int parentinfo[201] = { 0, };

void init_parent(int n) {
    for (int i = 1; i <= n; i++)
        parentinfo[i] = i;
}

int getParent(int parentinfo[], int a) {
    if (parentinfo[a] == a) return a;
    else
        return getParent(parentinfo, parentinfo[a]);

}

void uninParent(int parentinfo[], int a, int b) {
    a = getParent(parentinfo, a);
    b = getParent(parentinfo, b);

    if (a < b)
        parentinfo[b] = a;
    else
        parentinfo[a] = b;
}

int findParent(int parentinfo[], int n) {
    int answer = 0;
    for (int i = 1; i < n+1; i++) {
        if (parentinfo[i] != parentinfo[i + 1]) {
            answer++;
        }
    }
    return answer;
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    init_parent(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (computers[i][j] == 1) {
                if(i!=j)
                    uninParent(parentinfo, i+1, j+1);
            }
        }
    }

    answer = findParent(parentinfo, n);

    return answer;
}

int main() {
 //   vector<vector<int>> computers;

    vector<vector<int> > computers = { {1, 0, 0}, {0, 1, 0}, {0, 0, 1} };

    /*
    computers[1][1] = 1;
    computers[1][2] = 1;
    computers[1][3] = 0;

    computers[2][1] = 1;
    computers[2][2] = 1;
    computers[2][3] = 0;

    computers[3][1] = 0;
    computers[3][2] = 0;
    computers[3][3] = 1;
    */
    printf("%d\n", solution(3, computers));
}
