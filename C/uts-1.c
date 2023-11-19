#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int isCharInContainer(char container[], char ch, int size, int *index){
    for(int i = 0; i<size; i++){
        if(container[i] == ch){
            *index = i;
            return 1;
        }
    }
    return 0;
}

int main() {
    int n;
    char myString[100];
    scanf("%d", &n);
    scanf("\n");
    int counter = 0;
    for(int i=0; i<n; i++){
        scanf("%s", myString);
        //printf("myString: %s\n", myString);
        char unique_char[10];
        int unique_char_count[10];
        int containerSize = 0;
        int index;
        char hasil;
        for(int j=0; j < strlen(myString); j++){
            if(isCharInContainer(unique_char, myString[j], containerSize, &index)){
                unique_char_count[index] += 1;
            } else {
                unique_char[containerSize] = myString[j];
                unique_char_count[containerSize] = 1;
                containerSize++;
            }
        }
        //printf("%s", unique_char);
        for(int l=0; l<strlen(unique_char); l++){
            for(int k=0; k<strlen(unique_char); k++){
                if(l!=k){
                    if(unique_char_count[l] == unique_char_count[k]){
                        printf("triggered 1:%d:%d\n", l, unique_char_count[l]);
                        hasil = 'N';
                    } else {
                        printf("triggered 2:%d:%d\n", l, unique_char_count[l]);
                        hasil = unique_char[l];
                    }
                    //(unique_char_count[l] == unique_char_count[k]) ? hasil = {'N','/','A'} : hasil = unique_char[l];
                }
            }
        }
        printf("Case %d: %c", i+1, hasil);
        scanf("\n");
    }
    return 0;
}
