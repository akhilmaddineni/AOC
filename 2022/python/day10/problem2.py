ans = 0 

with open("input.txt",'r') as f : 
    ip = [ x.replace('\n','') for x in f.readlines()]
    pos = 1 
    cycle = 0 
    ans_pattern = [["." for _ in range(40)] for _ in range(6)]

    for line in ip : 
        cmd = line.split(" ")
        if cmd[0] == 'noop' :
            if cycle%40 in (pos-1,pos,pos+1) : 
                ans_pattern[(cycle)//40][cycle%40] = "█"
            cycle +=1
        else : 
            #check sprite pos 
            #edit the array
            if cycle%40 in (pos-1,pos,pos+1) : 
                ans_pattern[cycle//40][cycle%40] = "█"
            if (cycle+1)%40 in (pos-1,pos,pos+1) : 
                ans_pattern[(cycle+1)//40][(cycle+1)%40] = "█"
            cycle += 2
            #exec the instruction 
            pos += int(cmd[1])
    for a in ans_pattern :
        print("".join(a))



                
        
    
        
             
