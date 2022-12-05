ans  = 0 
with open("input_p1.txt",'r') as f : 
    b_map = {'X' : 'A',
             'Y' : 'B',
             'Z' : 'C'}
    val_map = {
        'X' : 1,
        'Y' : 2,
        'Z' : 3
    }
    for line in f : 
        choice_a,choice_b =map(str,line.rstrip().split())
        if choice_a == b_map[choice_b] : 
            ans += val_map[choice_b]+3
        elif (choice_b=='Y' and choice_a=='A') or (choice_b=='Z' and choice_a=='B') or (choice_b=='X' and choice_a=='C') : 
            ans += val_map[choice_b]+6
        else : 
            ans += val_map[choice_b] 
        
print(ans)
             
