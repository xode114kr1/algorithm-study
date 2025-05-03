#include <iostream>
#include <math.h>
using namespace std;

long min(long a, long b){
    if(a >= b)return b;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    return a;
}

int main(){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        long a, b, cmt = 1;
        cin >> a >> b;
        for(int j = min(a,b); j >= 1; j--){
            if(a % j == 0 and b % j == 0){
                a = a / j;
                b = b / j;
                cmt = cmt * j;
            }
        }
        cout << a * b * cmt << '\n'; 
    }
}