#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
   int i,rep,x;
   vector<int>v;
   cin >> rep;
   for(i = 0; i < rep; i++){
      cin >> x;
      v.push_back(x);
   }
   if(rep == 1)
      cout << x*x;
   else{
      sort(v.begin(),v.end());
      cout << v.front() * v.back();
   }
   return 0;
}