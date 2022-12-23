from collections import deque
ans  = '' 
with open("input_p1.txt",'r') as f : 
    raw_input = [x.replace('\n', ' ') for x in f.readlines()]
    #read stacks of cargo first 
    #len 3 for each input one space as delimiter 
    idx  = 0 
    #input_stack = [deque()]*(len(raw_input[0])//4) #this is not working correcty , deque object address is coming up as same
    input_stack = []
    for i in range(len(raw_input[0])//4): 
        input_stack.append(deque())
    print(raw_input[:4])
    for i in range(len(raw_input)) : 
        if raw_input[i+1] != ' ' : 
            stack_idx = 0
            for j in range(0,len(raw_input[i]),4) : 
                if raw_input[i][j:j+4] != '    ' : 
                    input_stack[stack_idx].appendleft(raw_input[i][j:j+4].rstrip().replace('[','').replace(']',''))
                stack_idx+=1 
        else :
            break
        idx += 1
    idx+=2 #next move instructions set from this index 
    #print(input_stack)
    #print(raw_input)
    for i in range(idx,len(raw_input)) : 
        instruction_arr = raw_input[i].split()
        #index 1,3,5 are POI 
        num_blocks = int(instruction_arr[1])
        source_idx = int(instruction_arr[3])-1
        dest_idx = int(instruction_arr[5])-1
        for j in range(num_blocks) : 
            #assuming no empty stack at all instances , i should write a check though
            input_stack[dest_idx].append(input_stack[source_idx].pop())
    print(input_stack)

for i in range(len(input_stack)) : 
    ans +=  input_stack[i].pop()  
        
print(ans)
             
