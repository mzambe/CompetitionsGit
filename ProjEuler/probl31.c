#include<stdio.h>
#include<stdlib.h>

#define N 200

int c[] = {0, 1, 2, 5, 10, 20, 50, 100}, p[8][N + 1];

int main(){
    int i, j, k, hwmany;

    for(i = 0; i <= N; i++)
        p[1][i] = 1;

    for(i = 2; i <= 7; i++){
        for(j = 0; j <= N; j++){
            p[i][j] = 0;
            hwmany = j / c[i];
            for(k = 0; k <= hwmany; k++){
                p[i][j] += p[i - 1][j - (k*c[i])];
            }
        }
    }

    printf("%d\n", p[7][N]);

    return 0;
}
