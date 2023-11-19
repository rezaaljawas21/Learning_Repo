#include <stdio.h>

int main() {
    int n, x, container = 0, total = 0, flag = 1;
    scanf("%d", &n);
    scanf("\n");
    for(int i=0; i<n; i++){
        if(i==(n-1)){
            scanf("%d", &x);
        } else {
            scanf("%d ", &x);
        }
        total += x;
    }
    //scanf("\n");
    //printf("%d", total);
    while (flag == 1){
        while((total/10)>1){
            container += total%10;
        }
        if(container/10>1){
            total = container;
        } else {
            flag = 0;
        }
    }
    printf("%d", container);
    
    return 0;
}