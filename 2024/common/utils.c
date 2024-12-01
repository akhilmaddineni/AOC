#include "utils.h"

char* read_file(const char* filename) {
    FILE* file = fopen(filename, "r");
    if (!file) {
        perror("Error opening file");
        return NULL;
    }

    // Seek to the end to determine file size
    fseek(file, 0, SEEK_END);
    long filesize = ftell(file);
    rewind(file);

    // Allocate buffer and read file content
    char* buffer = (char*)malloc(filesize + 1);
    if (!buffer) {
        perror("Error allocating memory");
        fclose(file);
        return NULL;
    }

    fread(buffer, 1, filesize, file);
    buffer[filesize] = '\0';

    fclose(file);
    return buffer;
}

char** split_string(const char* str, const char* delimiter, int* count) {
    if (!str || !delimiter || !count) return NULL;

    // Copy the input string to avoid modifying the original
    char* copy = strdup(str);
    if (!copy) return NULL;

    // Count tokens
    *count = 0;
    char* temp = copy;
    while ((temp = strstr(temp, delimiter))) {
        (*count)++;
        temp += strlen(delimiter);
    }
    (*count)++; // Add one for the last token

    // Allocate array for the tokens
    char** tokens = (char**)malloc((*count) * sizeof(char*));
    if (!tokens) {
        free(copy);
        return NULL;
    }

    // Split the string
    int index = 0;
    char* token = strtok(copy, delimiter);
    while (token) {
        tokens[index++] = strdup(token);
        token = strtok(NULL, delimiter);
    }

    free(copy);
    return tokens;
}

void free_string_array(char** array, int count) {
    if (!array) return;
    for (int i = 0; i < count; i++) {
        free(array[i]);
    }
    free(array);
}

char** split_by_space(const char* str, int* count) {
    if (!str || !count) return NULL;

    // Copy the input string to avoid modifying the original
    char* copy = strdup(str);
    if (!copy) return NULL;

    // Initialize token count and allocate space for pointers
    *count = 0;
    int capacity = 10; // Start with space for 10 tokens
    char** tokens = (char**)malloc(capacity * sizeof(char*));
    if (!tokens) {
        free(copy);
        return NULL;
    }

    // Tokenize the string
    char* token = strtok(copy, " ");
    while (token) {
        // Resize if necessary
        if (*count >= capacity) {
            capacity *= 2;
            char** new_tokens = (char**)realloc(tokens, capacity * sizeof(char*));
            if (!new_tokens) {
                free(copy);
                free(tokens);
                return NULL;
            }
            tokens = new_tokens;
        }

        // Add the token to the array
        tokens[*count] = strdup(token);
        (*count)++;
        token = strtok(NULL, " ");
    }

    free(copy);
    return tokens;
}

int compare_asc(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int compare_desc(const void* a, const void* b) {
    return (*(int*)b - *(int*)a);
}

