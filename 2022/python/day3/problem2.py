ans  = 0 
with open("input_p1.txt",'r') as f : 
    count = 0
    for line in f : 
        count +=1 
        if count%3 ==1 :
            lis_s = set(line.rstrip())
        elif count%3 ==2  :
            lis_s=lis_s.intersection(line.rstrip())
        else :
            lis_s=list(lis_s.intersection(line.rstrip()))
            if len(lis_s) !=0 : 
                s=ord(lis_s[0])
                if s > 96 : 
                    ans += s-96
                else : 
                    ans += s-64+26
      
print(ans)
             
