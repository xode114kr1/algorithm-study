#include <stdio.h>
#include <math.h>

int main() 
{
  int go,back,high,high_1,asd;
  scanf("%d %d %d",&go,&back,&high);
  high_1 = high - go;
  int assd = go-back;
  asd = abs(floor(-1.0*high_1/assd));
  printf("%d",asd+1);
  return 0;
}