#include<stdio.h>

int main()
{
    int n,i,k;
    int max, count;
    k = 1;
    int A[8];
    for(i = 0; i<9;i++)
    {
        scanf("%d",&A[i]);
    }
    max = A[0];
    for(i = 0; i<9;i++)
    {
        if(A[i]>max)
        {
            max = A[i];
            k = i+1;
        }
    }
    printf("%d\n%d",max,k );
    return 0;
}