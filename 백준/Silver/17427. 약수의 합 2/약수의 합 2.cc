using namespace std;
#include <iostream>

int main(){
  long long count = 0;
  int i,n;
  cin >> n;
  for(i = 1; i <=n;i++){
    count += (n/i)*i;
  }
  cout << count;
}