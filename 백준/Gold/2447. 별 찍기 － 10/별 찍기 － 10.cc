#include <iostream>
using namespace std;
void star10(int i, int j, int n);
int main(){
   int i,n,j;
   cin >> n;
   for(i = 0; i < n; i++){
      for(j = 0; j < n; j++){
         star10(i,j,n);
      }
      cout << "\n";
   }
}
void star10(int i, int j, int n){
   if((i/n)%3 == 1 && (j/n)%3 == 1)
   {
      cout << " ";
   }
   else if(n/3 == 0){
      cout << "*";
   }
   else
      star10(i,j,n/3);
}