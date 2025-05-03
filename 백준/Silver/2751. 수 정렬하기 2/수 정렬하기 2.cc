#include <stdio.h>
int tmp[1000000];

void merge(int A[],int L,int mid,int R);
void merge_sort(int A[],int L,int R);
int main()
{
  int rep,A[1000000],i;
  scanf("%d",&rep);
  for(i = 0; i<rep;i++)
    scanf("%d",&A[i]);
  merge_sort(A,0,rep-1);
  for(i = 0; i < rep; i++)
    printf("%d\n",A[i]);
}
void merge_sort(int A[],int L,int R)
{
  int mid;
  if(L<R)
  {
    mid = (L+R)/2;
    merge_sort(A,L,mid);
    merge_sort(A,mid+1,R);
    merge(A,L,mid,R);
  }
}

void merge(int A[],int L,int mid,int R)
{
  int i;
  int left = L,right = mid+1,k = L;
  while(left <= mid && right <= R)
    {
      if(A[left] <=A[right])
        tmp[k++] = A[left++];
      else
        tmp[k++] = A[right++];
    }
  if(left > mid)
  {
    for(i = right;i<=R;i++)
      tmp[k++] = A[i];
  }
  else
  {
    for(i = left;i<=mid;i++)
      tmp[k++] = A[i];
  }
  for(i = L;i<=R;i++)
    {
      A[i] = tmp[i];
    }
}