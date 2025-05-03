#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

void find_dw(vector<int> &v){
    int i,j,over = -100;
    for(i = 0; i < v.size(); i++){
        over += v[i];
    }
    for(i = 0; i < 8; i++){
        for(j = i+1; j < 9; j++){
            if(v[i]+v[j] == over){
                v.erase(v.begin() + i);
                v.erase(v.begin() + j-1);
                return;
            }
            else if(v[i]+v[j]> over){
                break;
            }
        }
    }
}
int main(){
    int i,n;
    vector<int> dwarf;
    for(i = 0; i < 9; i++){
        scanf("%d",&n);
        dwarf.push_back(n);
    }
    sort(dwarf.begin(),dwarf.end());
    find_dw(dwarf);
    for(i = 0; i < 7; i++){
        printf("%d\n",dwarf[i]);
    }
}