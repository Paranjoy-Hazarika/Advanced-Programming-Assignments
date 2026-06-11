#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    char *data;
    size_t length;
    size_t capacity;        
} StringBuffer;

StringBuffer* sb_init(size_t inital_capacity) {
    StringBuffer *sb = malloc(sizeof(StringBuffer));
    if (sb == NULL) return NULL;

    sb->data = malloc(inital_capacity);
    if (sb->data == NULL) {
        free(sb);
        return NULL;
    }

    sb->data[0] = '\0';
    sb->length = 0;
    sb->capacity = inital_capacity;

    return sb;
}

void sb_append(StringBuffer *sb, const char *str) {
    size_t append_len = strlen(str);
    size_t needed_capacity = sb->length + append_len + 1;

    if (needed_capacity > sb->capacity) {
        size_t new_capacity = sb->capacity * 2;

        if (new_capacity < needed_capacity) {
            new_capacity = needed_capacity;
        }

        char *temp = realloc(sb->data, new_capacity);
        if (temp == NULL) {
            printf("Failed to grow buffer!\n");
            return;
        }

        sb->data = temp;
        sb->capacity = new_capacity;
        printf("Buffer grew to %zu bytes\n", sb->capacity);
    }

    strcat(sb->data, str);
    sb->length += append_len;
}

void sb_free(StringBuffer *sb) {
    if (sb) {
        free(sb->data);
        free(sb);
    }
}

int main() {
    StringBuffer *my_sb = sb_init(2);
    if (!my_sb) return 1;

    printf("Initial Capacity: %zu\n", my_sb->capacity);

    sb_append(my_sb, "Hello, ");
    printf("String: %s | Length: %zu\n", my_sb->data, my_sb->length);

    sb_append(my_sb, " World!");
    printf("String: %s | Length: %zu\n", my_sb->data, my_sb->length);

    sb_free(my_sb);
    printf("\nMemory freed. Program finished.\n");

    return 0;
}