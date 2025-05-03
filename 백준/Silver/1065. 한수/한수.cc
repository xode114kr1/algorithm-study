#include <stdio.h>

void hansoo(int n);
int count = 0;
int main () 
{
    int n;
    scanf("%d",&n);
    for(int i =1;i<=n;i++)
    {
        hansoo(i);
    }
    printf("%d\n",count);
    return 0;
}


void hansoo (int n) 
{
    int a1,a2,a3;
    int i = 0;
    if(n==1000)
    {
        count +=0;
    }
    else if(n<100)
    {
        count += 1;
    }
    else
    {

        a1 = n%10;
        a2 = (n/10)%10;
        a3 = n/100;
        if(a3-a2 == a2 - a1)
        {
            count +=1;
        }
    }
    
}
