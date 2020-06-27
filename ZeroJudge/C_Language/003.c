#include <stdio.h>

int main(){
    int mouth, day;
    scanf("%d%d", &mouth, &day);
    if ((mouth*2+day) % 3 == 0)
        printf("普通\n");
    else if ((mouth*2+day) % 3 == 1)
        printf("吉\n");
    else
        printf("大吉\n");

    return 0;
}