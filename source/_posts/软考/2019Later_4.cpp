#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void strCompress(char *str){
    int i;
    char *p, tstr[11];
    char *s= str, *buf;
    if(strlen(str)<3)
        return;
        
    buf = (char*)malloc(strlen(str)*sizeof(char)+1);
    if(!buf)
        return;
    
    for(i = 0; *s;){
        int k = 1;
        buf[i++] = *s; //易错
        if(s[1] && *s == *(s+1)){ //难点
            k++;
            while(*s==*(s+k)) k++;
            sprintf(tstr, "%d", k);
            p = tstr;
            while(*p)
                buf[i++] = *p++;
        }
        s+=k;
    }
    buf[i] = '\0';
    strcpy(str, buf);

    free(buf);
}

int main(void) {
    char test[] = "abbbcdddddddeeed";
    printf("%s\n",test);
    strCompress(test);
    printf("%s\n",test);
    return 0;
}