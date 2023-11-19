#include <stdio.h>

int main() {
    int n; 
    scanf("%d", &n);
    scanf("\n");
    int array_kecepatan[n], array_waktu[n];
    for(int i=0; i<n; i++){
        scanf("%d %d", &array_kecepatan[i], &array_waktu[i]);
        //scanf("\n");
    }
    int total = 0;
    for(int i=0; i<n; i++){
        total += (array_kecepatan[i] * array_waktu[i]);
    }
    printf("%d km", total);
    return 0;
}