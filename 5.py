#include <stdio.h>
#include<stdlib.h>
int main() {
    // Write C code here
    int r,c,i,j,k,index=-1;
    printf("Enter row and col:");
    scanf("%d %d",&r,&c);
    printf("enter k:");
    scanf("%d",&k);
    int **mat=(int**)malloc(r*sizeof(int*));
    for(i=0;i<r;i++){
        mat[i]=(int*)malloc(c*sizeof(int));
    }
    printf("Enter the elements:");
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            scanf("%d",&mat[i][j]);
        }
    }
    for(i=0;i<r;i++){
        for(j=0;j<c;j++){
            if(mat[i][j]==k){
                index=j;
                break;
            }
        }
    }
    printf("Element %d found at column %d.",k,index);
}