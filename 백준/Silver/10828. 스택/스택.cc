#include <iostream>
#include <stack>
#include <string.h>
#include <string>
using namespace std;

int main(){
    stack<int>stack;
    int n,i,rep;
    char A[10];
    scanf("%d",&rep);
    for(i = 0; i < rep; i++){
        scanf("%s",A);
        if(strcmp(A,"push")==0){
            scanf("%d",&n);
            stack.push(n);
        }
        else if(strcmp(A,"pop")==0){
            if(stack.empty()==1)
                printf("-1\n");
            else{
                printf("%d\n",stack.top());
                stack.pop();
            }
        }
        else if(strcmp(A,"size")==0){
            printf("%d\n",stack.size());
        }
        else if(strcmp(A,"empty")==0){
            printf("%d\n",stack.empty());
        }
        else if(strcmp(A,"top")==0){
            if(stack.empty()==1)
                printf("-1\n");
            else{
                printf("%d\n",stack.top());
            }
        }
    }
}