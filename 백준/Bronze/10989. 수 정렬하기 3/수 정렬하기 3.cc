#include <stdio.h>

int main()
{
  int B[1000000] = {0, };
  int rep,i,j;
  scanf("%d",&rep);
  for(i = 0; i < rep; i++)
    {
      scanf("%d",&j);
      B[j]++;
    }
  for(i = 1; i <= 10001;i++)
    {
      if(B[i]==0)
        continue;
      for(j = 0;j<B[i];j++)
        printf("%d\n",i);
    }
}
