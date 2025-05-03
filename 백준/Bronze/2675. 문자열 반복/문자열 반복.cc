#include<stdio.h>


void asd(char A[],int n);
int main()
{
	int n,re, i,j,k;
	char S[10000];
	char P[10000];
	scanf("%d",&n);
	for(i = 0;i<n;i++)
	{
		scanf("%d",&re);
		scanf("%s",S);
		j = 0;
		while(S[j])
		{
			for(k = j*re; k < j*re+re; k++)
			{
				P[k] = S[j];
				printf("%c",P[k]);
			}
			j++;
		}
		printf("\n");
	}
}
