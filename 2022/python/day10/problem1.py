ans = 0 
#TODO : remove this shit 
def check_storage(cycle,flag_dic) : 

    if cycle in (20,60,100,140,180,220) : 
        return True, True,cycle
    elif cycle in (21,61,101,141,181,221) : 
        return True, True,cycle-1
    return False,False,cycle
with open("input.txt",'r') as f : 
    ip = [ x.replace('\n','') for x in f.readlines()]
    val = 1 
    cycle = 0 
    flag_dic = {}
    for line in ip : 
        cmd = line.split(" ")
        #print(cmd)
        if cmd[0] == 'noop' : 
            cycle += 1 
            flag,rm_val,store_cycle = check_storage(cycle,flag_dic)
            if  flag :
                if store_cycle not in flag_dic :
                    print(f"val : {val} cycle : {cycle} store_cycle : {store_cycle} ans push : {val*store_cycle}") 
                    flag_dic[store_cycle] = True
                    ans += val*store_cycle
        else : 
            val += int(cmd[1])
            cycle += 2
            flag,rm_val,store_cycle = check_storage(cycle,flag_dic)
            if flag :
                #remnant code - too lazy to remove
                if rm_val : 
                    val -= int(cmd[1])
                if store_cycle not in flag_dic :
                    print(f"val : {val} cycle : {cycle} store_cycle : {store_cycle} ans push : {val*store_cycle}")
                    flag_dic[store_cycle] = True
                    ans += val*store_cycle
                if rm_val : 
                    val += int(cmd[1])
    #print(flag_dic)
    print(ans)


                
        
    
        
             
