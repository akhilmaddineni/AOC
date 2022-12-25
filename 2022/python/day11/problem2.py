from collections import deque
import operator
with open("input.txt",'r') as f : 
    #for line in f : 
    raw_input = [x.replace("\n","") for x in f.readlines()]
    # get number of monkeys
    num_monkeys = raw_input.count("")+1 #delimiter is new line 
    print(num_monkeys)
    
    monkey_arr = [ deque() for _ in range(num_monkeys)]
    operation_arr = [[] for _ in range(num_monkeys)]
    test_div = [1 for _ in range(num_monkeys)]
    res_arr = [[i,i] for i in range(num_monkeys)] #true , false
    
    idx = 0
    # get each monkey starting item and operation
    # get each what monkey it can transfer to 
    for ele in raw_input :
        
        ele=ele.strip()
        ele = ele.split(" ")
        if ele[0] == "" : 
            idx += 1
            continue
        #print(ele)
        if ele[0] == 'Starting' : 
            for i in range(2,len(ele)) : 
                monkey_arr[idx].append(int(ele[i].rstrip(",")))
        elif ele[0] == 'Operation:' :
            operation_arr[idx].extend(ele[3:]) # after new = 
        elif ele[0] == 'Test:' :
            test_div[idx] = int(ele[-1])
        elif ele[1] == 'true:' : 
            res_arr[idx][0] = int(ele[-1])
        elif ele[1] == 'false:' : 
            res_arr[idx][1] = int(ele[-1])
    print(monkey_arr)
    print(operation_arr)
    print(test_div)
    print(res_arr)
    
    inspection_count = [0 for _ in range(num_monkeys)]
    operation_dict = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}
    
    #got help : how does this work ?
    mod = 1 
    for i in test_div :
        mod *= i
    #do the operations 10000 times 
    for _ in range(10000) : 
        for i in range(num_monkeys) : 
            for j in range(len(monkey_arr[i])) :
                inspection_count[i] += 1 
                oper = operation_arr[i]
                ele = monkey_arr[i].popleft()
                oper = list(map(lambda x: x.replace('old', str(ele)), oper))
                new_ele = operation_dict[oper[1]](int(oper[0]),int(oper[2]))%mod
                #check if new_ele is divisible by test_div
                if new_ele % test_div[i] == 0 : 
                    monkey_arr[res_arr[i][0]].append(new_ele)
                else : 
                    monkey_arr[res_arr[i][1]].append(new_ele)
    inspection_count=sorted(inspection_count)
    print(inspection_count[-1]*inspection_count[-2])
                 

            
