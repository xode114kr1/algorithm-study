#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

void compression(vector<pair<int,int>>&v);
bool compare(pair<int,int>p1,pair<int,int>p2){
  return p1.second < p2.second;
}
vector<pair<int,int>>tmpv;
int main(){
  int i,rep;
  cin >> rep;
  pair<int,int>tmp;
  vector<pair<int,int>>v;
  for(i = 0; i < rep; i++){
    cin >> tmp.first;
    tmp.second = i;
    v.push_back(tmp);
  }
  sort(v.begin(),v.end());
  compression(v);
  sort(v.begin(),v.end(),compare);
  for(i = 0; i < rep; i++){
    cout << v[i].first << " "; 
  }
}
void compression(vector<pair<int,int>>&v){
  tmpv.clear();
  tmpv.assign(v.begin(), v.end());
  tmpv[0].first = 0;
  int k = 0, i;
  for(i = 1; i < v.size(); i++){
    if(v[i].first != v[i-1].first){
      k++;
    }
    tmpv[i].first = k;
  }
  v.clear();
  v.assign(tmpv.begin(),tmpv.end());
}