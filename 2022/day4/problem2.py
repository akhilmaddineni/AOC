ans  = 0 
with open("input_p1.txt",'r') as f : 
    for line in f : 
        line  = line.rstrip()
        a,b   = line.split(",")
        a_arr = list(map(int,a.split('-')))
        b_arr = list(map(int,b.split('-')))
        flag = True
        if a_arr[1] < b_arr[0] or b_arr[1] < a_arr[0] : 
            flag = False
        if flag : 
            ans+=1
        
print(ans)
             
