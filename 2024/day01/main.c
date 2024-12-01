#include <stdlib.h>
#include <stdio.h>
#include "utils.h"

int main()
{   

    // Read the input file
    char* input = read_file("day01/input.txt");
    if (!input) {
        return 1;
    }

    // Split the input into lines
    int line_count = 0;
    char** lines = split_string(input, "\n", &line_count);
    //printf("%d",line_count);

    int* left_list = (int*)malloc(sizeof(int)*line_count);
    int* right_list = (int*)malloc(sizeof(int)*line_count);

    for(int i=0 ; i<line_count ; i++){
        int count_nums = 0;
        char** nums = split_string(lines[i],"   ",&count_nums); 
        //count nums for this input is 2 
        left_list[i] = atoi(nums[0]); 
        right_list[i] = atoi(nums[1]);
        printf("%d %d \n",left_list[i],right_list[i]); 
        free(nums);
    }

    qsort(left_list,line_count,sizeof(int),compare_asc);
    qsort(right_list,line_count,sizeof(int),compare_asc); 

    int ans = 0 ; 

    for(int i=0 ; i<line_count ; i++){
        ans += abs(right_list[i]-left_list[i]);
    }

    printf("Day 01 Ans Part 1 : %d\n",ans);

    //part 2 

    GHashTable* hash_table = g_hash_table_new(g_int_hash, g_int_equal);

    //count frequency on right list 
    for(int i=0 ; i<line_count ; i++){
        int* key = &right_list[i]; 
        int* value = g_hash_table_lookup(hash_table, key);
        if (value) {
            (*value)++;
        }
        else {
            int *freq = g_malloc(sizeof(int)); 
            *freq = 1; 
            g_hash_table_insert(hash_table,key,freq);
        }
    }

    int ans2 = 0 ; 
    
    for(int i=0 ; i<line_count ; i++){
        //lookup the ele in hash 
        int* key = &left_list[i]; 
        int* value = g_hash_table_lookup(hash_table, key);
        if(value){
            ans2 += left_list[i]*(*value);
        }
    }
    printf("Day 01 Ans Part 2 : %d\n",ans2);



    //free memory
    
    // Free the memory allocated for the hash table values
    GList *keys = g_hash_table_get_keys(hash_table);
    for (GList *l = keys; l != NULL; l = l->next) {
        int* key = (int *)l->data;
        int* value = g_hash_table_lookup(hash_table, key);
        if (value) {
            g_free(value);  // Free the allocated memory for the frequency count
        }
    }

    g_list_free(keys);  // Free the list of keys
    
    free(left_list);
    free(right_list); 
    g_hash_table_destroy(hash_table);
    free(input);
    // Free memory allocated for lines
    for (int i = 0; i < line_count; i++) {
        free(lines[i]);
    }
    free(lines);

    return 0;
}