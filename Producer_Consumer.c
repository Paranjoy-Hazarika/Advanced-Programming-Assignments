#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define TOTAL_ITEMS 10

int buffer[BUFFER_SIZE];
int count = 0;

pthread_mutex_t lock;
pthread_cond_t cond_is_full;
pthread_cond_t cond_is_empty;

void* producer(void* arg) {
    for (int i = 1; i <= TOTAL_ITEMS; i++) {
        pthread_mutex_lock(&lock);

        while (count == BUFFER_SIZE) {
            printf("[Producer] Buffer full. Waiting...\n");
            pthread_cond_wait(&cond_is_full, &lock);
        }

        buffer[count] = i;
        printf("[Producer] Produced item %d | Items in buffer: %d\n", i, count + 1);
        count++;

        pthread_cond_signal(&cond_is_empty);

        pthread_mutex_unlock(&lock);
        sleep(1);
    }
    return NULL;
}

void* consumer(void* arg) {
    for (int i = 1; i <= TOTAL_ITEMS; i++) {
        pthread_mutex_lock(&lock);

        while (count == 0) {
            printf("[Consumer] Buffer empty. Waiting...\n");
            pthread_cond_wait(&cond_is_empty, &lock);
        }

        int item = buffer[count - 1];
        printf("[Consumer] Consumed item %d | Items left in buffer: %d\n", item, count - 1);
        count--;

        pthread_cond_signal(&cond_is_full);

        pthread_mutex_unlock(&lock);
        usleep(150000);
    }
    return NULL;
}

int main() {
    pthread_t prod_thread, cons_thread;

    pthread_mutex_init(&lock, NULL);
    pthread_cond_init(&cond_is_full, NULL);
    pthread_cond_init(&cond_is_empty, NULL);

    pthread_create(&prod_thread, NULL, producer, NULL);
    pthread_create(&cons_thread, NULL, consumer, NULL);

    pthread_join(prod_thread, NULL);
    pthread_join(cons_thread, NULL);

    pthread_mutex_destroy(&lock);
    pthread_cond_destroy(&cond_is_full);
    pthread_cond_destroy(&cond_is_empty);

    printf("Simulation finished cleanly.\n");
    return 0;
}