#include <stdio.h>
#include <string.h>

int count;
int recursion(const char *s, int l, int r){
   count++;
   if(l >= r) return 1;
   else if(s[l] != s[r]) return 0;
   else return recursion(s, l+1, r-1);
}

int isPalindrome(const char *s){
    return recursion(s, 0, strlen(s)-1);
}

int main(){
   char A[1000];
   int i,rep;
   scanf("%d",&rep);
   for(i = 0; i < rep; i++){
      count = 0;
      scanf("%s", A);
      int k = isPalindrome(A);
      printf("%d %d\n",k,count);
   }
}