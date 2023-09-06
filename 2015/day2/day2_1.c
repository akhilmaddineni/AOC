#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

#define MIN(x,y) (((x) < (y)) ? (x) : (y))

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
    long long int ans_final = 0; 

    while(fgets(line,sizeof(line),fp))
    {
        int arr[] = {0,0,0};
        int idx = 0;
        int ans = 0;
        int ans_offset = INT_MAX;
        for(int i = 0; line[i] != '\0' && line[i] != '\n'; i++)
        {
            if(line[i] == 'x') idx++;
            else 
            {
                arr[idx] = arr[idx]*10 + (line[i]-48) ; 
            }
        } 
        //printf("%d %d %d \n",arr[0],arr[1],arr[2]);
        for(int i=0;i<3;i++)
        {
            ans_offset = MIN(ans_offset,arr[i%3]*arr[(i+1)%3]) ;    
            ans += 2*arr[i%3]*arr[(i+1)%3] ; 
        }
        //printf("%d\n",ans+ans_offset);
        ans_final += ans+ans_offset;
    }
    printf("%lld",ans_final);
    return 0;

}