#include<stdio.h>
int decomposition(int n);
int num_d(int n);

int main()
{
  int n;
  scanf("%d",&n);
  printf("%d",decomposition(n));
  return 0;
}

int decomposition(int n)
{
  int asd = 0;
  for(int i=n;i>=1;i--)
  {
    int sum = i;
    int k = i;
    int d = num_d(i);
    if(true)
    {
      for(int j = 0; j<d;j++)
      {
        sum = sum + k%10;
        k = k/10;
      }
    }
    if(n == sum)
    asd = i;
  }
  return asd;
}

int num_d(int n)
{
  int count = 0;
  if(n<10)
  return 1;
  else
  {
    while(n>=10)
    {
      n = n/10;
      count += 1;
    }
    return count+1;
  }
}
