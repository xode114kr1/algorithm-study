#include <stdio.h>

int asd(int n);
int main()
{
  int i, n;
  int count = 0;
  int A[100000];
  scanf("%d",&n);
  for(i = 0; i< n;i++)
    {
      scanf("%d",&A[i]);
      count += asd(A[i]);
    }
  printf("%d",count);
}
int asd(int n)
{
  int i;
  int count = 0;
  if(n == 1)
    return 0;
  if(n==2)
    return 1;
  for(i = 2; i<n;i++)
    {
      if(n%i==0)
        return 0;
    }
  return 1;
}