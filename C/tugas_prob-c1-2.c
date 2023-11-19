#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    char *str, c;
    int i = 0, j = 1;

    str = (char*)malloc(sizeof(char));

    while (c != '\n') {
        // read the input from keyboard standard input
        c = getc(stdin);

        // re-allocate (resize) memory for character read to be stored
        str = (char*)realloc(str, j * sizeof(char));

        // store read character by making pointer point to c
        str[i] = c;

        i++;
        j++;
    }
    
    str[i] = '\0';

    i = 0;
    j = 0;
    
    for(int i=0; i<(sizeof(str)+2); i++){
        str[i] = str[i] + 3;
    }

    printf("%s", str);
    
    free(str);
    
    return 0;
}