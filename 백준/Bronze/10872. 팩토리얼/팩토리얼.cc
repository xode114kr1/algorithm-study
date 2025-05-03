#include <iostream>
int pac(int n);
using namespace std;
int main(){
  int i;
  cin >> i;
  int k = pac(i);
  cout << k;
}
int pac(int n){
  if(n > 1)
    return n*pac(n-1);
  return 1;
}