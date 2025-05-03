#include <stdio.h>

struct coor{
int x;
int y;
};

typedef struct coor COOR;
COOR tmp[100000];

void merge(COOR A[],int L,int mid,int R);
void mergesort(COOR A[],int L,int R);
int main()
{
  COOR A[100000];
  int rep,i;
  scanf("%d",&rep);
  for(i = 0; i<rep;i++){
    scanf("%d %d",&A[i].x,&A[i].y);
  }
  mergesort(A,0,rep-1);
  for(i = 0; i<rep;i++){
    printf("%d %d\n",A[i].x,A[i].y);
  }
}
void mergesort(COOR A[],int L,int R){
  int mid = (L+R)/2;
  if(L<R){
    mergesort(A,L,mid);
    mergesort(A,mid+1,R);
    merge(A,L,mid,R);
  }
}
void merge(COOR A[],int L,int mid,int R){
  int i = L;
  int j = mid+1;
  int k = L;
  int z;
  while(i<=mid&&j<=R){
    if(A[i].x < A[j].x)
      {
        tmp[k].x = A[i].x;
        tmp[k++].y = A[i++].y;
      }
    else if(A[i].x > A[j].x)
      {
        tmp[k].x = A[j].x;
        tmp[k++].y = A[j++].y;
      }
    else{
      if(A[i].y < A[j].y)
        {
          tmp[k].x = A[i].x;
          tmp[k++].y = A[i++].y;
        }
      else{
        tmp[k].x = A[j].x;
        tmp[k++].y = A[j++].y;
      }
    }
  }
  if(i>mid){
    for(z = j; z<=R;z++){
      tmp[k].x = A[z].x;
      tmp[k++].y = A[z].y;
    }
  }
  else{
    for(z = i; z<=mid;z++){
      tmp[k].x = A[z].x;
      tmp[k++].y = A[z].y;
    }
  }
  for(z = L;z<=R;z++){
    A[z].x = tmp[z].x;
    A[z].y = tmp[z].y;
  }
}
