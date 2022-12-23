 
with open("input_p1.txt",'r') as f : 
    for line in f : 
        line=line.rstrip() 
        for i in range(len(line)-4) : 
            if len(set(line[i:i+4])) == 4 : 
                print(i+4) 
                break
        
