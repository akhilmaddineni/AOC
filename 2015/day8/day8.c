#include <stdlib.h>
#include <stdio.h>

int caluculate_chars(char* line)
{
    //printf("%s\n",line);
    int num_chars = 0 ; // total number of chars 
    int valid_chars = 0 ; //valid chars after removing escape chars
    for(int i = 0; line[i] != '\0' && line[i] != '\n'; i++)
    {
        num_chars++;
        if(line[i] == '\\') 
        {
            if(line[i+1] == 'x')
            {
                num_chars += 3; 
                valid_chars++;
                i += 3; 
            }
            else
            {
                num_chars++;
                valid_chars++;
                i+=1;
            }
        }
        else
        {
            valid_chars++;
        }
    }
    valid_chars -= 2 ; // remove double quotes
    //printf("%d \t %d \n",num_chars,valid_chars); 
    return num_chars-valid_chars;
}

int reencode_chars(char* line)
{
    int num_chars = 0;
    int encoded_chars = 0; 
    for(int i = 0; line[i] != '\0' && line[i] != '\n'; i++)
    {
        if(line[i] == '\\' || line[i] == '"')
        {
            encoded_chars++;
        }
        num_chars++;
        encoded_chars++;
    }
    encoded_chars += 2; //adding double quotes
    //printf("%d \t %d \n",num_chars,encoded_chars); 
    return encoded_chars-num_chars;
}


int main()
{
    FILE *fp = fopen("input.txt","r");
    if(NULL == fp)
    {
        printf("Error in opening the file \n");
        exit(1);
    }
    char line[100];
    int ans_problem1 = 0;
    int ans_problem2 = 0; 

    while(fgets(line,sizeof(line),fp))
    {
        ans_problem1 += caluculate_chars(line);
        ans_problem2 += reencode_chars(line);
    }
    printf("problem1 : %d \n",ans_problem1);
    printf("problem2 : %d \n",ans_problem2);
    return 0;
}