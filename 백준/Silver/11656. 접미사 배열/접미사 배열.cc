#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
    string str;
    vector<string> vec;
    cin >> str;
    for(int i = 0; i < str.size(); i++){
        vec.push_back(str.substr(i, str.size()));
    }
    sort(vec.begin(), vec.end());
    for(int i = 0; i < str.size(); i++){
        cout << vec[i] << '\n';
    }
}