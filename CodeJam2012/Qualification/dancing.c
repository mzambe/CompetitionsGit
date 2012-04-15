#include<stdio.h>
#include<stdlib.h>

long long int scores[100];

int main(){
    long long int T, N, S, p, score, i, j, divthr, modthr, res;

    scanf("%lld", &T);
    for(i = 1; i <= T; ++i){
        scanf("%lld %lld %lld", &N, &S, &p);
        res = 0;
        for(j = 0; j < N; ++j){
            scanf("%lld", &score);// (scores + j));
            divthr = score / 3;
            modthr = score % 3;
            if (divthr >= p){
                ++res;
            }
            else{
                if (modthr == 1){
                    if ((divthr + 1) >= p)
                        ++res;
                }
                else if(modthr == 2){
                    if ((divthr + 1) >= p)
                        ++res;
                    else if ((divthr + 2) >= p)
                        if (S){
                            --S;
                            ++res;
                        }
                }
                else{
                    if (divthr > 0) {
                        if ((divthr + 1) >= p){
                            if (S){
                                --S;
                                ++res;
                            }
                        }
                    }
                }
            }
        }

        printf("Case #%lld: %lld\n", i, res);
    }

    return 0;
}
