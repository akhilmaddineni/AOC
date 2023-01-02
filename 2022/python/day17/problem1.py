from copy import deepcopy

input_arr = [
    [[0,0,1,1,1,1,0]],
    [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,0,0,1,0,0,0]
    ],
    [   [0,0,1,1,1,0,0],
        [0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0]

    ],
    [
        [0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0]
    ],
    [
        [0,0,1,1,0,0,0],
        [0,0,1,1,0,0,0]
    ]
]

num_blocks = [4,5,5,4,4] #num of blocks in each input arr 

# padding = [
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0]
# ]

def check_top(result_arr) : 
    top = result_arr[-1]
    for ele in top : 
        if ele == 1 : 
            return True
    return False

def caluculate_block_indexes(result,ip_idx) : 
    block_index_arr = []
    row_idx = len(result)-1 
    if ip_idx == 0 :
        #[0,0,1,1,1,1,0]
        block_index_arr.extend([[row_idx,2],
                                [row_idx,3],
                                [row_idx,4],
                                [row_idx,5]])
    elif ip_idx == 1: 
        # [0,0,0,1,0,0,0],
        # [0,0,1,1,1,0,0],
        # [0,0,0,1,0,0,0]
        block_index_arr.extend([[row_idx,3],
                                [row_idx-1,2],
                                [row_idx-1,3],
                                [row_idx-1,4],
                                [row_idx-2,3]])
    elif ip_idx == 2: 
        # [0,0,0,0,1,0,0],
        # [0,0,0,0,1,0,0],
        # [0,0,1,1,1,0,0]
        block_index_arr.extend([[row_idx,4],
                                [row_idx-1,4],
                                [row_idx-2,2],
                                [row_idx-2,3],
                                [row_idx-2,4]])
    elif ip_idx == 3:
        # [0,0,1,0,0,0,0],
        # [0,0,1,0,0,0,0],
        # [0,0,1,0,0,0,0],
        # [0,0,1,0,0,0,0]
        block_index_arr.extend([[row_idx,2],
                                [row_idx-1,2],
                                [row_idx-2,2],
                                [row_idx-3,2]])
    elif ip_idx == 4 : 
        # [0,0,1,1,0,0,0],
        # [0,0,1,1,0,0,0]
        block_index_arr.extend([[row_idx,2],
                                [row_idx,3],
                                [row_idx-1,2],
                                [row_idx-1,3]])
    else : 
        raise Exception("input index provided is not correct !")
    return block_index_arr
        

def right_shift_block(result_arr,block_idxs) :
    #check validity 
    valid = True
    #print(result_arr)
    new_block_indexes = []
    for each_idx in block_idxs : 
        #print(each_idx)
        if each_idx[1]+1 < len(result_arr[0]) :
            if [each_idx[0],each_idx[1]+1] not in block_idxs:
                if result_arr[each_idx[0]][each_idx[1]+1] !=0 :
                    valid = False
                    break
        else : 
            valid = False
            break
    if valid : 
        for i in range(len(block_idxs)) : 
            new_block_indexes.append([block_idxs[i][0],block_idxs[i][1] +1])
    else : new_block_indexes = block_idxs
    return new_block_indexes
        

def left_shift_block(result_arr,block_idxs) :
    #check validity 
    valid = True
    new_block_indexes = []
    #print(result_arr)
    for each_idx in block_idxs : 
        #print(each_idx)
        if each_idx[1]-1 >= 0 :
            if [each_idx[0], each_idx[1] - 1] not in block_idxs:
                if result_arr[each_idx[0]][each_idx[1]-1] !=0 :
                    valid = False
                    break
        else : 
            valid = False
            break
    if valid :
        for i in range(len(block_idxs)):
            new_block_indexes.append([block_idxs[i][0], block_idxs[i][1] - 1])
    else : new_block_indexes = block_idxs
    return new_block_indexes

def check_hit(result_arr,block_idxs) : 
    for each_idx in block_idxs :
        if [each_idx[0]-1,each_idx[1]] not in block_idxs:
            if result_arr[each_idx[0]-1][each_idx[1]] !=0:
                return True
    return False

def drop_block(old_block_idxs) :
    #check for check hit before this call
    new_block_indexes = []
    for i in range(len(old_block_idxs)) :
        new_block_indexes.append([old_block_idxs[i][0]-1,old_block_idxs[i][1]])
    return new_block_indexes

def update_result_arr(result_arr,old_block_idx,new_block_idx) :
    for ele in old_block_idx:
        result_arr[ele[0]][ele[1]] = 0
    for ele in new_block_idx :
        result_arr[ele[0]][ele[1]] = 1
    return  result_arr

if __name__ == "__main__" :
    f=open("input.txt","r")
    dir_arr = [x for x in f.readlines()[0].rstrip()]
    #print(dir_arr)
    f.close()
    result = [[1,1,1,1,1,1,1]] #note : height-1 due to rock base 
    #while True :
    #loop dir arr infinitely 
    #when top of arr has a rock add padding and start processing next element in ip arr 
    #process until it hits a rock on top of the result arr 
    #pop out any empty rows from the top/end 
    #break when 2022 rocks have fallen
    dir_arr_count = 0
    ip_count = 0
    dir_arr_len = len(dir_arr)
    ip_len = len(input_arr)
    rock_fall = 0
    while True : 
        if check_top(result) : 
            #add padding and start process 
            result.extend([[0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0]])
            #caluculate block indexes
            inp_arr_copy = deepcopy(input_arr[ip_count%ip_len])
            result.extend(inp_arr_copy)
            block_indexes = caluculate_block_indexes(result,ip_count%ip_len)
            #total_blocks += num_blocks[ip_count%ip_len]
            ip_count += 1
            #process until it hits a rock on top of the result arr
            while True :
                #new_block_indexes = block_indexes
                if dir_arr[dir_arr_count%dir_arr_len] == '>' :
                    #right shift
                    new_block_indexes=right_shift_block(result,block_indexes)
                    result = update_result_arr(result,block_indexes,new_block_indexes)
                elif dir_arr[dir_arr_count%dir_arr_len] == '<' : 
                    #left shift block
                    new_block_indexes=left_shift_block(result,block_indexes)
                    result = update_result_arr(result, block_indexes, new_block_indexes)
                dir_arr_count += 1
                block_indexes = new_block_indexes
                #drop down
                if check_hit(result,new_block_indexes) :
                    break
                else :
                    new_block_indexes = drop_block(block_indexes)
                    result = update_result_arr(result, block_indexes, new_block_indexes)
                    block_indexes=new_block_indexes
            rock_fall +=1

        else : 
            #remove all empty rows from top
            while True : 
                result.pop()
                if check_top(result) : 
                    break
            if rock_fall >= 2022 :
                break
    print(len(result)-1)
