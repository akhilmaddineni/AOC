ans  = [] 
with open("input_p1.txt",'r') as f : 
    cur  = 0 
    for line in f : 
        if line.rstrip() != "" : 
            cur += int(line.rstrip())
        else : 
            ans.append(cur)
            cur=0
ans.sort()
print(sum(ans[-3:]))
print(ans[-3:])
             
