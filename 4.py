#include <stdio.h>
#include<stdlib.h>
int main() {
    // Write C code here
    int n,k,i,index=-1;
    printf("Enter n:");
    scanf("%d",&n);
    int *arr=(int*)malloc(n*sizeof(int));
    printf("Enter array elements:");
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter k:");
    scanf("%d",&k);
    for(i=0;i<n;i++){
        if(arr[i]==k){
            index=i;
        }
    }
    printf("Index: %d",index);
}