#include <stdio.h>
#include <stdlib.h>

void constantSpace(int n) {
    int a = 10;
    int b = n;
    int c = a + b;

    printf("O(1) Space used: %zu bytes\n", sizeof(a) + sizeof(b) + sizeof(c));
}

void linearSpace(int n) {
    int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) return;

    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }

    printf("O(n) Space used (approx): %zu bytes\n", n * sizeof(int));

    free(arr);
}

void quadraticSpace(int n) {
    size_t totalBytes = 0;
    int **matrix = (int **)malloc(n * sizeof(int *));
    if (matrix == NULL) return;

    totalBytes += n * sizeof(int);

    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)malloc(n * sizeof(int));
        if (matrix[i] == NULL) return;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = i + j;
            totalBytes += n * sizeof(int);
        }
    }

    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }

    printf("O(n^2) Space used (approx): %zu bytes\n", totalBytes);

    free(matrix);

    return;
}

int main() {
    int sizes[] = {100, 500, 1000};
    int numSizes = sizeof(sizes) / sizeof(sizes[0]);

    for (int i = 0; i < numSizes; i++) {
        int n = sizes[i];
        printf("\nInput Size: %d\n", n);

        constantSpace(n);
        linearSpace(n);
    }

    return 0;
}