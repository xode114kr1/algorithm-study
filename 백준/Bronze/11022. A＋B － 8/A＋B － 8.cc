#include<stdio.h>

int main()
{
  int i,rep,a,b;
  scanf("%d",&rep);
  for(i = 1; i<=rep;i++)
    {
      scanf("%d %d",&a,&b);
      printf("Case #%d: %d + %d = %d\n",i,a,b,a+b);
    }
  return 0;
}