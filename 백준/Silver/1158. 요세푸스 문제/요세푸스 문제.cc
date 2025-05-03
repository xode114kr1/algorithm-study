#include <iostream>
#include <queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n,k;
    cin >> n >> k;
    queue<int> que;
    for(int i = 1; i <= n; i++){
        que.push(i);
    }
    cout << '<';
    for(int i = 0; i < n-1; i++){
        for(int j = 0; j < k-1; j++){
            que.push(que.front());
            que.pop();
        }
        cout << que.front();
        cout << ", ";
        que.pop();
    }
    cout << que.front() << '>';
}