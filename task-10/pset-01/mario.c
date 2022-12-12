#include <stdio.h>

int main(){
    int rows;
    printf("Enter number of rows: ");
    scanf("%d", &rows);
    for (int i = 0; i < rows; i++){
        for (int j = 0; j < rows; j++){
            if (j < rows-i-1){
                printf(" ");
            }
            else{
                printf("$");
            }
        }
        printf("\n");
    }
    return 0;
}