ans  = 0 
with open("input_p1.txt",'r') as f : 
    for line in f : 
        line  = line.rstrip()
        a,b   = line.split(",")
        a_arr = list(map(int,a.split('-')))
        b_arr = list(map(int,b.split('-')))
        flag = True
        #TODO : can be optimized 
        if a_arr[1]-a_arr[0] <= b_arr[1]-b_arr[0] : 
            for ele in range(a_arr[0],a_arr[1]+1) : 
                if not ( ele >=b_arr[0] and ele <=b_arr[1] ): 
                    flag=False
        elif b_arr[1]-b_arr[0] <= a_arr[1]-a_arr[0] : 
            for ele in range(b_arr[0],b_arr[1]+1) : 
                if not ( ele >=a_arr[0] and ele <=a_arr[1] ): 
                    flag=False
        else :
            flag=False
        if flag : 
            ans+=1
             
        
print(ans)
             
