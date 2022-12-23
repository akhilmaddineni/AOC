ans  = 0 
with open("input_p1.txt",'r') as f : 
    cur  = 0 
    for line in f : 
        if line.rstrip() != "" : 
            cur += int(line.rstrip())
        else : 
            if cur > ans : 
                ans = cur
            cur=0
print(ans)
