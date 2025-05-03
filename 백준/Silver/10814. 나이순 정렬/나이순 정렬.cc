#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

bool compare(pair<int,string>p1,pair<int,string>p2){
   return p1.first < p2.first;
}
int main(){
   int i, rep;
   cin >> rep;
   vector<pair<int,string>>p;
   pair<int,string>tmp;
   for(i = 0; i<rep;i++){
      cin >> tmp.first >> tmp.second;
      p.push_back(tmp);
   }
   stable_sort(p.begin(),p.end(),compare);
   for(i = 0; i<rep;i++){
      cout << p[i].first << " " << p[i].second << "\n";
   }
   return 0;
}