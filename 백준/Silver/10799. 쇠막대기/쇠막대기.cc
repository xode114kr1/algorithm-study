#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string str;
    stack<char> st;
    cin >> str;
    int ans = 0;
    for(int i = 0; i < str.size(); i++){
        if(str[i] == '(')
            st.push(i);
        else if(str[i] == ')'){
            if(str[i-1] == '('){
                st.pop();
                ans += st.size();
            }
            else{
                st.pop();
                ans++;
            }
        }
    }
    cout << ans;
}