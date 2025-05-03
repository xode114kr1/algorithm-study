#include<stdio.h>

int main()
{
    int hou, min, time;
    scanf("%d %d",&hou, &min);
    scanf("%d", &time);
    min += time;
    while(min >= 60)
    {
        min -= 60;
        hou += 1;
    }
    while(hou >= 24)
    {
        hou -= 24;
    }
    printf("%d %d",hou,min);
    return 0;
}