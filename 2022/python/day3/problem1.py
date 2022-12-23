ans  = 0 
with open("input_p1.txt",'r') as f : 
    for line in f : 
        lis_s = list(set(line.rstrip()[:(len(line.rstrip())//2)]).intersection(line.rstrip()[(len(line.rstrip())//2):]))
        if len(lis_s) !=0 : 
            s=ord(lis_s[0])
            if s > 96 : 
                ans += s-96
            else : 
                ans += s-64+26
      
print(ans)
             
