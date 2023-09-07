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
    int total_vertexes = 0 ; 
    char c; 

    vertex santa; 
    santa.x = 0;
    santa.y = 0;

    vertex arr[5000]; // arbitary value size array to store visited points 
    arr[0] = santa; 
    count++;

    vertex robo_santa ; 
    robo_santa.x = 0; 
    robo_santa.y = 0; 

    while((c = fgetc(fp)) != EOF)
    {   
        if (total_vertexes%2 == 0 )
        {
            if(c == '^')
            {
                santa.y++;
            }
            else if ( c ==  'v')
            {
                santa.y--;
            }
            else if ( c == '<')
            {
                santa.x--;
            }
            else if (c == '>')
            {
                santa.x++;
            }
            if (!isVisited(arr,count,santa))
            {
                arr[count] = santa;
                count++;
            }
        }
        else 
        {
            if(c == '^')
            {
                robo_santa.y++;
            }
            else if ( c ==  'v')
            {
                robo_santa.y--;
            }
            else if ( c == '<')
            {
                robo_santa.x--;
            }
            else if (c == '>')
            {
                robo_santa.x++;
            }
            if (!isVisited(arr,count,robo_santa))
            {
                arr[count] = robo_santa;
                count++;
            }
        }
        total_vertexes++ ; 
    }
    printf("%d",count); 
    return 0; 
}