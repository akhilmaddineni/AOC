#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <glib.h>

typedef long long LL;

// Reads the content of a file into a dynamically allocated buffer.
// Returns the content as a null-terminated string, or NULL on error.
char* read_file(const char* filename);

// Splits a string into an array of strings based on a delimiter.
// Returns the array of strings, and sets *count to the number of elements.
// The caller is responsible for freeing the returned array and its elements.
char** split_string(const char* str, const char* delimiter, int* count);

// Frees the memory allocated for an array of strings.
void free_string_array(char** array, int count);

char** split_by_space(const char* str, int* count);

//quick sort utility
int compare_asc(const void* a, const void* b); 

int compare_desc(const void* a, const void* b);

#endif // UTILS_H
