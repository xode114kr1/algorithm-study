#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    stack<char> left;
    stack<char> right;
    string str;
    int n;
    cin >> str;
    for(int i = 0; i < str.size(); i++)
        left.push(str[i]);
    cin >> n;
    for(int i = 0; i < n; i++){
        char cmd, x;
        cin >> cmd;
        if(cmd == 'L' and !left.empty()){
            right.push(left.top());
            left.pop();
        }
        else if(cmd == 'D' and !right.empty()){
            left.push(right.top());
            right.pop();
        }
        else if(cmd == 'B' and !left.empty())
            left.pop();
        else if(cmd == 'P'){
            cin >> x;
            left.push(x);
        }
    }
    while(!left.empty()){
        right.push(left.top());
        left.pop();
    }
    while(!right.empty()){
        cout << right.top();
        right.pop();
    }
}