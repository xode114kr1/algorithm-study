#include <stdio.h>
#include <math.h>

int max(int a,int b);
int change(int n,int d);
int num_d(int n);
int main()
{
    int a1,a2;
    scanf("%d %d",&a1,&a2);
    printf("%d",max(change(a1,num_d(a1)),change(a2,num_d(a2))));
    return 0;
}

int num_d(int n)
{
    int i = 0;
    while(n != 0)
    {
        n = n/10;
        i++;
    }
    return i;
}
int change(int n,int d)
{
    int i;
    int total = 0;
    for(i = d-1;i >= 0;i--)
    {
        total += n%10*pow(10.0, 1.0*i);
        n = n/10;
    }
    return total;
}
int max(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;
}