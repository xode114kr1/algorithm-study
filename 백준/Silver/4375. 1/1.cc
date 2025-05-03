#include <iostream>
using namespace std;
int main(){
   int n,k,ans;
   while(cin >> n){
      k = 1;
      ans = 1;
      while(1){
         if(ans%n == 0){
            break;
         }
         else{
            ans = ans*10+1;
            ans = ans%n;
            k++;
         }
      }
      cout << k << "\n";
   }
}