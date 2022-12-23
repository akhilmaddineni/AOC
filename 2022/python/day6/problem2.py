 
with open("input_p1.txt",'r') as f : 
    for line in f : 
        line=line.rstrip() 
        for i in range(len(line)-14) : 
            if len(set(line[i:i+14])) == 14 : 
                print(i+14) 
                break
        
             
