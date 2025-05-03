#include <iostream>
#include <string>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string str;
    getline(cin, str);
    for(int i = 0; i < str.size(); i++){
        if(str[i] >= 'A' && str[i] <= 'M' || str[i] >= 'a' && str[i] <= 'm')
            cout << char(str[i] + 13);
        else if(str[i] >= 'N' && str[i] <= 'Z' || str[i] >= 'n' && str[i] <= 'z')
            cout << char(str[i] - 13);
        else
            cout << char(str[i]);
    }
}