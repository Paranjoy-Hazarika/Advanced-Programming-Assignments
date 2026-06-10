#include <stdio.h>
#include <time.h>

#define MAX 20000

int arr[MAX];

void constantTime() {
    int x = arr[0];
}

void linearTime(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
}

void quadraticTime(int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            count += arr[i] * arr[j];
        }
    }
}

int main() {
    clock_t start, end;
    double time_taken;

    for (int i = 0; i < MAX; i++) {
        arr[i] = i;
    }

    for (int n = 1000; n <= 5000; n += 1000) {

        printf("\n==============================\n");
        printf("Input Size: %d\n", n);

        start = clock();
        constantTime();
        end = clock();
        time_taken = (double)(end - start) / CLOCKS_PER_SEC;
        printf("Time taken for O(1)  : %f seconds\n", time_taken);

        start = clock();
        linearTime(n);
        end = clock();
        time_taken = (double)(end - start) / CLOCKS_PER_SEC;
        printf("Time taken for O(n)  : %f seconds\n", time_taken);

        start = clock();
        quadraticTime(n);
        end = clock();
        time_taken = (double)(end - start) / CLOCKS_PER_SEC;
        printf("Time taken for O(n^2): %f seconds\n", time_taken);
    }

    return 0;
}