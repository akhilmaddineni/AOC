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
    int ans = 0;
    int count = 0;
    char c;
    while((c = fgetc(fp)) != EOF)
    {   count++;
        if(c == '(') ans++;
        else if (c == ')') ans--;
        // break for problem 2 
        if(ans<0) 
        {
            printf("%d\n",count);
            break; 
        } 
    }
    printf("%d",ans);
    return 0;

}