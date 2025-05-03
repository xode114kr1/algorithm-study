#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
using namespace std;
stack<int> st;
vector<char> v;
int main() {
	ios_base::sync_with_stdio(false), cin.tie(NULL);
	int n,cnt=1;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		int x;
		cin >> x;
		while (cnt <= x) {
			v.push_back('+');
			st.push(cnt);
			cnt++;
		}

		if(x == st.top()) {
			st.pop();
			v.push_back('-');
		}
		else {
			cout << "NO";
			return 0;
		}
	}
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << "\n";
	}
}