using namespace std;
#include <iostream>

int ans;
void QCD(int x, int y);
int main(){
   int x,y,i,tmp;
   cin >> x >> y;
   if(y > x){
      tmp = x;
      x = y;
      y = tmp;
   }
   QCD(x,y);
   cout << ans << "\n" << x*y/ans;
}
void QCD(int x, int y){
   if(x%y == 0){
      ans = y;
      return;
   }
   QCD(y,x%y);
}