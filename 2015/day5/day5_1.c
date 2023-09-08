#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

bool checkVowel(char c)
{
    if( 
        c == 'a' ||
        c == 'e' ||
        c == 'i' ||
        c == 'o' ||
        c == 'u'
    ) return true;
    return false;
}

bool checkBlacklist(char a,char b)
{
    if(a == 'a' && b == 'b') return true;
    if(a == 'c' && b == 'd') return true;
    if(a == 'p' && b == 'q') return true;
    if(a == 'x' && b == 'y') return true;
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

    //read lines 
    char line[100];

    int nice_strings = 0;

    while(fgets(line,sizeof(line),fp))
    {
        int vowel_count = 0;
        int i = 0 ;
        bool is_nice = true ; 
        bool char_repeat = false ; 
        for(i = 0; line[i+1] != '\0' && line[i+1] != '\n'; i++)
        {
            if (checkVowel(line[i])) vowel_count++;
            if (checkBlacklist(line[i],line[i+1]))
            {
                is_nice = false ; 
                break;
            }
            if(line[i] == line[i+1])
            {
                char_repeat = true;
            }

        }
        if(checkVowel(line[i])) vowel_count++;
        if ( vowel_count >= 3 && char_repeat && is_nice)
        {
            nice_strings++;
        }
    }
    printf("%d",nice_strings);
    return 0;

}