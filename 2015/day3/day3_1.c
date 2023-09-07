#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct vertex
{
    int x; 
    int y;
}vertex;

bool isVisited(vertex arr[],int count,vertex point)
{
    for(int i = 0 ; i<count; i++) // linear search but otherwise i need to implement a hashmap (not today)
    {
        if(arr[i].x == point.x && arr[i].y == point.y)
        {
            return true;
        }
    }
    return false;
}

int main()
{
    FILE *fp = fopen("input.txt","r");
    if(NULL == fp)
    {
        printf("Error in opening the file \n");
        exit(1);
    }
    int count = 0 ; 
    char c; 
    vertex point; 
    point.x = 0;
    point.y = 0;
    vertex arr[5000]; // arbitary value size array to store visited points 
    arr[0] = point; 
    count++;
    while((c = fgetc(fp)) != EOF)
    {   
        if(c == '^')
        {
            point.y++;
        }
        else if ( c ==  'v')
        {
            point.y--;
        }
        else if ( c == '<')
        {
            point.x--;
        }
        else if (c == '>')
        {
            point.x++;
        }
        if (!isVisited(arr,count,point))
        {
            arr[count] = point;
            count++;
        }
    }
    printf("%d",count); 
    return 0; 
}