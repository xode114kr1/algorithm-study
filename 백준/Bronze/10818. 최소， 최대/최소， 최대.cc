#include<stdio.h>

int main()
{
    int n,i;
    int max, min;
    int A[1000000];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d", &A[i]);
    }
    min = A[0];
    max = A[0];
    for(i = 0; i<n;i++)
    {
        if(A[i]<min)
            min = A[i];
        if(A[i]>max)
            max = A[i];
    }
    printf("%d %d",min, max);
    return 0;
}