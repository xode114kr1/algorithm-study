#include <stdio.h>


void swap(int A[100000],int n);
int main()
{
  int rep;
  int cut;
  int sum = 0;
  int A[100000] ={0, };
  scanf("%d %d",&rep,&cut);
  for(int i = 0; i<rep;i++)
    {
      scanf("%d",&A[i]);
      sum += A[i];
    }
  swap(A,rep);
  printf("%d",A[rep-cut]);
}
void swap(int A[100000], int n)
{
  int i,j,tmp,min,t;
  for(i = 0; i<n;i++)
    {
      t = i;
      min = A[i];
      for(j = i; j<n;j++)
        {
          if(min > A[j])
          {
            min = A[j];
            t = j;
          }
        }
      tmp = A[i];
      A[i] = min;
      A[t] = tmp;
    }
}