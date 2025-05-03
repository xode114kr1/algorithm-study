#include <iostream>
using namespace std;

int n_digit(int n);
int syom(int n, int dig);
int main(){
   int n,i,count = 0;
   cin >> n;
   for(i = 666; count < n; i++){
      count += syom(i,n_digit(i));
   }
   cout << i-1;
}
int syom(int n, int dig){
   int i, cnt = 0;
   for(i = 0; i < dig; i++){
      if(n%10 == 6){
         cnt++;
      }
      else{
         cnt = 0;
      }
      n = n/10;
      if(cnt == 3){
         return 1;
      }
   }
   return 0;
}
int n_digit(int n){
   int i = 1;
   while(n >= 10){
      n = n / 10;
      i++;
   }
   return i;
}