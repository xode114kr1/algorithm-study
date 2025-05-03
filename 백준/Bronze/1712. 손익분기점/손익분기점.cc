#include<stdio.h>
#include<math.h>

int main()
{
  int sta, mad, sel;
  scanf("%d %d %d", &sta,&mad,&sel);
  int asd = floor(1.0*sta/(sel - mad))+1;
  if(asd >= 0)
    printf("%d",asd);
  else
    printf("-1");
  return 0;
}