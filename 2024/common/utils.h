#ifndef UTILS_H
#define UTILS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Reads the content of a file into a dynamically allocated buffer.
// Returns the content as a null-terminated string, or NULL on error.
char* read_file(const char* filename);

// Splits a string into an array of strings based on a delimiter.
// Returns the array of strings, and sets *count to the number of elements.
// The caller is responsible for freeing the returned array and its elements.
char** split_string(const char* str, const char* delimiter, int* count);

// Frees the memory allocated for an array of strings.
void free_string_array(char** array, int count);

#endif // UTILS_H
