#include <stdio.h>
#include <string.h>

void reverse(char A[100000]);
void bigsum(char A[100000],char B[100000],char C[100000]);
int main() 
{
  int i = 0;
  char A[100000] = {0, };
  char B[100000] = {0, };
  char C[100000] = {0, };
  scanf("%s %s",A,B);
  if(strlen(A)>strlen(B))
  {
    reverse(B);
    reverse(A);
    for(i = strlen(B); i < strlen(A);i++)
      {
        B[i] = '0';
      }
  }
  else if(strlen(B)>strlen(A))
  {
    reverse(A);
    reverse(B);
    for(i = strlen(A); i < strlen(B);i++)
      {
        A[i] = '0';
      }
  }
  else
  {
    reverse(A);
    reverse(B);
  }
  bigsum(A,B,C);
  reverse(C);
  printf("%s",C);
}

void reverse(char A[100000])
{
  int i = 0;
  int len = strlen(A);
  int tmp[100000];
  while(A[i])
    {
      tmp[len-i-1] = A[i];
      i++;
    }
  i = 0;
  while(tmp[i])
    {
      A[i] = tmp[i];
      i++;
    }
}

void bigsum(char A[100000],char B[100000],char C[100000])
{
  int i = 0;
  int up = 0;
  while(A[i]||B[i]||up==1)
    {
      if(A[i]==0)
        A[i] = '0';
      if(B[i]==0)
        B[i]='0';
      if(A[i]+B[i]+up-96>9)
      {
        C[i] = A[i]+B[i]+up-58;
        up = 1;
      }
      else
      {
        C[i] = A[i]+B[i]+up-48;
        up = 0;
      }
      i++;
    }
}