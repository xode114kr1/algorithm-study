#include <stdio.h>

int main(void)
{
  int num;
  scanf("%d",&num);
  int a = num;
  int count = 0;
  while(1)
    {
      if(num < 10)
      {
        num = 11*num;
      }
      else
      {
        num = num%10*10+(num%10+num/10)%10;
      }
      count++;
      if(a==num)
        break;
    }
  printf("%d",count);
}