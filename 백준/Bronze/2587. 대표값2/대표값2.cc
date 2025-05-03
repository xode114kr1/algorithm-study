#include <stdio.h>
#include <string.h>

void swap(int A[100000],int n);
int main()
{
  int sum = 0;
  int A[100000] ={0, };
  for(int i = 0; i<5;i++)
    {
      scanf("%d",&A[i]);
      sum += A[i];
    }
  swap(A,5);
  printf("%d %d",sum/5,A[2]);
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