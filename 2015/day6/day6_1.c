#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


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

void turn_bits_on(bitfield field[] , coordinates left_top, coordinates right_bottom)
{

}

void turn_bits_off(bitfield field[] , coordinates left_top, coordinates right_bottom)
{

}

void toggle_bits(bitfield field[] , coordinates left_top, coordinates right_bottom)
{
    
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
    memset(field,0,sizeof(field)); 

    while(fgets(line,sizeof(line),fp))
    {
        char *words = strtok(line," ") ; 
        int count = 0; 
        bool toggle_flag  = false ; 
        bool turn_on = false;
        

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
            if(toggle_flag)
            {
                toggle_bits(field,left_top,right_bottom); 
            }
            if(turn_on)
            {
                turn_bits_on(field,left_top,right_bottom);
            }
            else 
            {
                turn_bits_off(field,left_top,right_bottom);
            }

            count++;
            //get next word 
            words = strtok(NULL," "); 
            
            
        }
    }
    printf("%ld",sizeof(uint32_t));
    return 0;

}