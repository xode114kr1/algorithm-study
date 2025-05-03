#include<stdio.h>

int main(){
    char A[51];
    int rep;
    scanf("%d", &rep);
    for(int i = 0; i < rep; i++){
        scanf("%s", A);
        int j = 0;
        int index = 0;
        bool proposition = 1;
        while(A[j]){
            if(A[j] == '(')
                index++;
            else if(A[j] == ')')
                index--;
            j++;
            if(index < 0){
                proposition = 0;
                break;
            }
        }
        if(proposition == 1 && index == 0)
            printf("YES\n");
        else
            printf("NO\n");
    }
}