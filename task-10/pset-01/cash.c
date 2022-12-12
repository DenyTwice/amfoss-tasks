#include <stdio.h>
#include <math.h>
int main(){
    float cash;
    printf("Enter recieved money: ");
    scanf("%f", &cash);
    int dollar = (int)cash;
    // printf("Dollar is %i",dollar);
    int change = round((cash - dollar)* 100);

    // printf("Change is %d", change);

    int coinsIncDollar = 4 * dollar;
    int coins = 0;
    while (change > 0){
        if (change >= 25){
            coins += 1;
            change -= 25;
        }
        else if (change >= 10){
            coins += 1;
            change -= 10;
        }
        else if (change >= 5){
            coins += 1;
            change -= 5;
        }
        else if (change >= 1){
            coins += 1;
            change -= 1;
        }
    
        
    }
    printf("Number of coins to give: %d", coins);
    // printf("%d", coins+ coinsIncDollar);
    
}