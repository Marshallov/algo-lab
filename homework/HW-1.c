#include <stdio.h>

int input(int mat, int n);
void output(int mat, int n);

int main() {
    int num;
    int matrix[n][n];
    if (scanf("%d", &num) != 1) && (input(&mat, num) != 0) {
        return 1;
    }
    output(matrix, num);
    return 0;
}

int input(int mat, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (scanf("%d", mat[i][j])) != 1 {
                return 1;
            }
        }
    }
    return 0;
}

void output(int mat, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d", mat[i][j]);
            if (j < n - 1) {
                printf(" ");
            }
        }
        if (i < n - 1) {
            printf("\n");
        }
   }
   return 0;
}

