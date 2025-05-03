#include <iostream>
#include <string>
#include <stack>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cout << fixed;
    cout.precision(2);
    int N, y;
    int A[26];
    double x, n1, n2;
    char k = 0;
    string cmd;
    stack<double> num;
    cin >> N;
    cin >> cmd;
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    int i = 0;
        while(cmd[i]){
        if (cmd[i] == '*')
        {
            n1 = num.top();
            num.pop();
            n2 = num.top();
            num.pop();
            num.push(n1*n2);
        }
        else if (cmd[i] == '/')
        {
            n1 = num.top(); 
            num.pop();
            n2 = num.top();
            num.pop();
            num.push(n2/n1); 
        }
        else if (cmd[i] == '+')
        {
            n1 = num.top();
            num.pop();
            n2 = num.top();
            num.pop();
            num.push(n1+n2);
        }
        else if (cmd[i] == '-')
        {
            n1 = num.top();
            num.pop();
            n2 = num.top();
            num.pop();
            num.push(n2-n1);
        }
        if(cmd[i] >= 65 && cmd[i] <= 90){
            num.push(A[cmd[i]-65]);
        }
        i++;
    }
    cout << num.top();
}