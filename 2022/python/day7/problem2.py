
class NBTree : 
    def __init__(self,val,parent) : 
        self.val = val #int when its a file , str when dir 
        self.child = []
        self.parent = parent
    
    def add_node(self,data,parent_ptr) :
        node = NBTree(data,parent_ptr)
        self.child.append(node)
    
def sum_space_dir(node) : 
    #get the data at the particular level + any leaf nodes of sub dirs 
    count = 0
    sum_arr = []
    for i in node.child : 
        #print(i.val)
        if type(i.val) == int :
            count += i.val
        else : 
            #loop through all the child nodes of the directory. 
            count_tmp,sum_arr_tmp  = sum_space_dir(i)
            count += count_tmp
            sum_arr.extend(sum_arr_tmp)
    sum_arr.append(count)
    return (count,sum_arr)
                            
 
with open("input_p1.txt",'r') as f : 
    for line in f : 
        raw_input = [x.replace("\n","") for x in f.readlines()]
        # ignore line 1 - cd /
        # ls - next x number of lines store the data 
        # cd move up or down the tree - store parent node 
        root = NBTree("root",None)
        temp = root
        for i in range(1,len(raw_input)) : 
            #print(f"raw input {raw_input[i]}")
            if "$ ls" in raw_input[i] : 
                pass
            elif "$ cd .." in raw_input[i] : 
                #print("moving up the tree")
                temp=temp.parent
            elif "$ cd" in raw_input[i] : 
                #move to the child node 
                node_name = raw_input[i].split(" ")[-1]
                for i in temp.child : 
                    if type(i.val) == str : 
                        if node_name==i.val : 
                            #print(f"child node name {node_name}")
                            temp=i
            else : 
                #two possibilites - either directory or file 
                
                if "dir" in raw_input[i] : 
                    node_name = raw_input[i].split(" ")[-1]
                    #print(f"adding directory {node_name}")
                    node = temp.add_node(node_name,temp) 
                else: 
                    node_val = int(raw_input[i].split()[0]) 
                    #print(f"adding {node_val}")
                    temp.add_node(node_val,temp)
        total_sum,sum_dir = sum_space_dir(root)
        sum_dir.sort()
        ans = sum_dir[-1]
        for i in reversed(sum_dir): 
            if total_sum-i <= 40000000 : 
                if i<=ans : 
                    ans=i 
                else : 
                    break
            else : 
                break
        print(ans)
        
            
                
                
                
                
        
        
        
        
             
