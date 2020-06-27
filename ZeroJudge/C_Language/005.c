#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    int i, a, b, c, d;

    for (i=0; i<num; i++){
        scanf("%d%d%d%d", &a, &b, &c, &d);
        if (d-c == c-b)
            printf("%d %d %d %d %d\n", a, b, c, d, d+b-a);
        else
            printf("%d %d %d %d %d\n", a, b, c, d, d*b/a);
    }

    return 0;
}