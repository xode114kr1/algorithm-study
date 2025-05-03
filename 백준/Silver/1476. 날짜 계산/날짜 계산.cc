#include <stdio.h>

int main(){
    int E,S,M,i = 1;
    scanf("%d %d %d",&E,&S,&M);
    if(E==15)
        E = 0;
    if(S == 28)
        S = 0;
    if(M == 19)
        M = 0;
    while(1){
        if(i%15 == E){
            if(i%28 == S){
                if(i%19 == M){
                    break;
                }
            }
        }
        i++;
    }
    printf("%d",i);
}