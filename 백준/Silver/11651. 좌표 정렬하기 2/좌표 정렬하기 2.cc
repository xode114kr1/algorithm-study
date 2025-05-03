#include <stdio.h>

struct coor{
int x;
int y;
};

typedef struct coor COOR;
COOR tmp[100000];

void merge(COOR A[],int L,int mid,int R);
void mergesort(COOR A[],int L,int R);

int main(){
  COOR A[100000];
  int rep,i;
  scanf("%d",&rep);
  for(i = 0;i<rep;i++){
    scanf("%d %d",&A[i].x, &A[i].y);
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
void merge(COOR A[],int L, int mid,int R){
  int left = L, right = mid+1, k = L, i;
  while(left<=mid&&right<=R){
    if(A[left].y < A[right].y){
      tmp[k].x = A[left].x;
      tmp[k++].y = A[left++].y;
    }
    else if(A[left].y > A[right].y){
      tmp[k].x = A[right].x;
      tmp[k++].y = A[right++].y;
    }
    else{
      if(A[left].x < A[right].x){
        tmp[k].x = A[left].x;
        tmp[k++].y = A[left++].y;
      }
      else{
        tmp[k].x = A[right].x;
        tmp[k++].y = A[right++].y;
      }
    }
  }
  if(left > mid){
    for(i = right; i<=R;i++){
      tmp[k].x = A[i].x;
      tmp[k++].y = A[i].y;
    }
  }
  else{
    for(i = left; i<=mid;i++){
      tmp[k].x = A[i].x;
      tmp[k++].y = A[i].y;
    }
  }
  for(i = L;i<=R;i++){
    A[i].x = tmp[i].x;
    A[i].y = tmp[i].y;
  }
}