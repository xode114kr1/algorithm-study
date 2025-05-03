#include<stdio.h>


int main()
{
	int i,j;
	int A[100][100];
	int max, row, col;
	for(i = 0; i<9;i++)
	{
		for(j=0;j<9;j++)
		{
			scanf("%d",&A[i][j]);
		}
	}
	max = A[0][0];
	row = 1, col = 1;
	for(i = 0; i<9;i++)
	{
		for(j=0;j<9;j++)
		{
			if(A[i][j]>max)
			{
				max = A[i][j];
				row = i+1;
				col = j+1;
			}
		}
	}
	printf("%d\n%d %d",max,row,col);
	return 0;
}