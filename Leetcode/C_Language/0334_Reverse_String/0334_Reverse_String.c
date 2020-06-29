#include <stdio.h>
#include <string.h>

void reverseString(char* s, int sSize){    
    for(int i=0;i<sSize/2;i++){
        char tmp;
        tmp=s[i];
        s[i]=s[sSize-i-1];
        s[sSize-i-1]=tmp;
    }
}

/*======================================================================*/

int main(){
    char s[5]="hello";
    reverseString(s, strlen(s));
    printf("%s\n", s);
    return 0;
}
