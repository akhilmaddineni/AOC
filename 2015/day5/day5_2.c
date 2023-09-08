#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>


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

    while(fgets(line,sizeof(line),fp))
    {
        int vowel_count = 0;
        int i = 0 ;

        bool char_repeat = false ; 
        bool overlap = false;
        for(i = 2; line[i] != '\0' && line[i] != '\n'; i++)
        {
            if(line[i-2] == line[i]) 
            {
                char_repeat = true; //let it run to find string length
            }  
        }
        // i now contains length of str 
        printf("len : %d ",i);
        for (int j = 0; j<i-1; j++)
        {
            for(int k = j+2 ; k<i ; k++)
            {
                if((line[j] == line[k]) && (line[j+1] == line[k+1]))
                {
                    overlap = true ; 
                    break;
                }
            }
            if(overlap) break;
        }

        if ( overlap && char_repeat)
        {
            nice_strings++;
            printf("nice string : %s \n ",line);
        }
        else 
        {
            printf("naughty string : %s \n ",line);
        }
    }
    printf("%d",nice_strings);
    return 0;

}