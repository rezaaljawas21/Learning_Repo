#include <stdio.h>

int main() {
    int n; 
    scanf("%d", &n);
    scanf("\n");
    int array_nilai_uang[n], array_waktu[n];
    int array_persentase_bunga[n];
    for(int i=0; i<n; i++){
        scanf("%d %d %d", &array_nilai_uang[i], &array_persentase_bunga[i], &array_waktu[i]);
        //scanf("\n");
    }

    for(int i=0; i<n; i++){
        int tabungan = array_nilai_uang[i];
        printf("Case #%d\n", i+1);
        for(int j=0; j<array_waktu[i]; j++){
            tabungan = tabungan + (tabungan * 0.8 * (((1.0*array_persentase_bunga[i])/100)/12));
            printf("%d %d\n", j+1, tabungan);
        }
    }
    return 0;
}