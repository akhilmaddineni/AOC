#include <stdlib.h>
#include <stdio.h>

int main()
{
    FILE *fp = fopen("input.txt","r");
    if(NULL == fp)
    {
        printf("Error in opening the file \n");
        exit(1);
    }
    char line[100];

    while(fgets(line,sizeof(line),fp))
    {
        
    }

}