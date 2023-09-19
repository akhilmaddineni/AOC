#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <stdint.h>
#include <inttypes.h>

//this could probably be done with math with tracking the on and off bits between ranges but we are too deep in logic to back out now :) 
//TODO : complete this bitwise solution
typedef struct coordinates
{
    int x;
    int y;
} coordinates;

#define ARR_SIZE 32 

typedef struct bitfield
{
    uint32_t bitfield_arr[ARR_SIZE] ; 
}bitfield;

void toggle_arr(uint8_t arr[1000][1000],coordinates left_top,coordinates right_bottom)
{
    printf("Toggle coordinates x1 = %d,y1 = %d - x2 = %d,y2 = %d\n",left_top.x,left_top.y,right_bottom.x,right_bottom.y);
    for(int i=left_top.x;i<=right_bottom.x;i++)
    {
        for(int j= left_top.y; j<=right_bottom.y;j++)
        {
            arr[i][j] += 2 ; 
        }
    }

}

void turn_on_arr(uint8_t arr[1000][1000],coordinates left_top,coordinates right_bottom)
{   printf("Turing on coordinates x1 = %d,y1 = %d - x2 = %d,y2 = %d\n",left_top.x,left_top.y,right_bottom.x,right_bottom.y);
    for(int i=left_top.x;i<=right_bottom.x;i++)
    {
        for(int j= left_top.y; j<=right_bottom.y;j++)
        {
            //printf("%d\t%d\n",i,j);
            arr[i][j] += 1 ; 
        }
    }

}

void turn_off_arr(uint8_t arr[1000][1000],coordinates left_top,coordinates right_bottom)
{
    printf("Turing off coordinates x1 = %d,y1 = %d - x2 = %d,y2 = %d\n",left_top.x,left_top.y,right_bottom.x,right_bottom.y);
    for(int i=left_top.x;i<=right_bottom.x;i++)
    {
        for(int j= left_top.y; j<=right_bottom.y;j++)
        {
            if(arr[i][j] > 0)
            arr[i][j] -= 1 ; 
        }
    }

}

long int count_set_bits(uint8_t arr[1000][1000])
{
    long int count = 0;
    for(int i=0;i<1000;i++)
    {
        for(int j=0;j<1000;j++)
        {
            count += arr[i][j]; 
        }
    }
    return count;
}


int main()
{
    FILE *fp = fopen("input.txt","r");
    if(NULL == fp)
    {
        printf("Error in opening the file \n");
        exit(1);
    }

    //read lines 
    char line[100];

    int nice_strings = 0;

    //define co-ordinates bitfield 
    bitfield field[999]; 
    //set to 0  

    //partial changes without bitfields 
    uint8_t bit_array[1000][1000] = {0} ; 

    memset(field,0,sizeof(field)); 
    //memset(bit_array,0,sizeof(bit_array));

    while(fgets(line,sizeof(line),fp))
    {
        char *words = strtok(line," ") ; 
        int count = 0; 
        bool toggle_flag  = false ; 
        bool turn_on = false;
        
        printf("%s\n",line);
        coordinates left_top ; 
        coordinates right_bottom ;

        while( words != NULL )
        {
            if(count == 0 && strcmp(words, "toggle") == 0 )
            {
                toggle_flag = true;
            }
            if(count == 1 && toggle_flag == false && strcmp(words,"on") == 0 )
            {
                turn_on = true;
            }
            
            if ((count == 2 && toggle_flag == false) || (count == 1 && toggle_flag == true))
            {
                left_top.x = 0; 
                left_top.y = 0;
                int idx = 0 ; 
                for(int i = 0; words[i] != '\0' && words[i] != '\n'; i++)
                {
                    if(words[i] == ',') 
                    {
                        idx++;
                        continue;
                    }

                    if(idx == 0)
                    {
                        left_top.x = left_top.x*10 + (words[i]-48) ; 
                    }
                    else 
                    {
                        left_top.y = left_top.y*10 + (words[i]-48) ; 
                    }
                }
            }

            if ((count == 4 && toggle_flag == false) || (count == 3 && toggle_flag == true))
            {
                right_bottom.x = 0; 
                right_bottom.y = 0;
                int idx = 0 ; 
                for(int i = 0; words[i] != '\0' && words[i] != '\n'; i++)
                {
                    if(words[i] == ',') 
                    {
                        idx++;
                        continue;
                    }
                    if(idx == 0)
                    {
                        right_bottom.x = right_bottom.x*10 + (words[i]-48) ; 
                    }
                    else 
                    {
                        right_bottom.y = right_bottom.y*10 + (words[i]-48) ; 
                    }
                }
            }

            //set bits based on instruction

            count++;
            //get next word 
            words = strtok(NULL," "); 
            
            
        }

        if(toggle_flag)
        {
            toggle_arr(bit_array,left_top,right_bottom); 
        }
        else if(turn_on)
        {
            turn_on_arr(bit_array,left_top,right_bottom);
        }
        else 
        {
            turn_off_arr(bit_array,left_top,right_bottom);
        }


    }
    printf("%ld",count_set_bits(bit_array));
    return 0;

}