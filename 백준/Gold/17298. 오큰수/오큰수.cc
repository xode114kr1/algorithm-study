#include <iostream>
#include <stack>
using namespace std;
int A[1000001];
int ans[1000001];
int main(){
    int n;

    stack<int> st;
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> A[i];
    }
    for(int i = n-1; i >= 0; i--){
        while(!st.empty() && st.top() <= A[i])
            st.pop();
        if(st.empty())
            ans[i] = -1;
        else
            ans[i] = st.top();
        st.push(A[i]);
    }
    for(int i = 0; i < n; i++){
        cout << ans[i] << ' ';
    }
}