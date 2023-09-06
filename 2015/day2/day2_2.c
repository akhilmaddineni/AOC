#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

#define MIN(x,y) (((x) < (y)) ? (x) : (y))

void swap(int *a,int *b)
{
    int temp = *a;
    *a =*b;
    *b=temp; 
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
    long long int ans_final = 0; 

    while(fgets(line,sizeof(line),fp))
    {
        int arr[] = {0,0,0};
        int idx = 0;
        int ribbon_wrap = 0;
        for(int i = 0; line[i] != '\0' && line[i] != '\n'; i++)
        {
            if(line[i] == 'x') idx++;
            else 
            {
                arr[idx] = arr[idx]*10 + (line[i]-48) ; 
            }
        } 
        printf("%d %d %d \n",arr[0],arr[1],arr[2]);
        //sort the array
        if(arr[0]>arr[2]) swap(&arr[0],&arr[2]);
        if(arr[0]>arr[1]) swap(&arr[0],&arr[1]);
        if(arr[1]>arr[2]) swap(&arr[1],&arr[2]);
        
        ribbon_wrap += 2*arr[0]+2*arr[1];
        ribbon_wrap += arr[0]*arr[1]*arr[2];
        ans_final += ribbon_wrap;
    }
    printf("%lld",ans_final);
    return 0;

}