#include <stdio.h>

int main()
{
    int n;
    int A[100];
    int a;
    int count = 0;
    int i;
    scanf("%d", &n);
    for(i = 0; i<n; i++)
    {
        scanf("%d",&A[i]);
    }
    scanf("%d",&a);
    for(i = 0; i < n;i++)
    {
        if(a==A[i])
        {
            count++;
        }
    }
    printf("%d",count);
    return 0;
}

