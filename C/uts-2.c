#include <stdio.h>

void findBiggest(int array_[], int n, int *column, int *row){
    int biggest = 0,hasil;
    for(int i=0; i<(n*n); i++){
        if(biggest > array_[i]){
            biggest = biggest;
        } else {
            biggest = array_[i];
            *column = i%n;
            *row = i/n;
        }
    }
}

int main() {
    int n, column, row, counter = 0;
    scanf("%d", &n);
    scanf("\n");
    int array_[n][n];
    int streamlined_array[n*n];
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if((i==(n-1)) && (j==(n-1))){
                scanf("%d", &array_[i][j]);
            } else {
                scanf("%d ", &array_[i][j]);
            }
            streamlined_array[counter] = array_[i][j];
            counter++;
        }
    }
    findBiggest(streamlined_array, n, &column, &row);
    printf("ans: ");
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            ((i!=(column))&&(j!=(row))) ? printf("%d ", array_[i][j]) : printf("");
        }
    }
    return 0;
}