import json

def compare_lists(list1,list2) :
    #three cases : continue , pass , fail 
    #continue -0  pass - 0xff fail - 0xf 
    ans=0
    if len(list1) == 0 and len(list2) > 0  :
        return 0xFF
    for i in range(min(len(list1),len(list2))) : 
        if type(list1[i]) == int and type(list2[i]) == int :
            if list1[i] == list2[i] :
                continue
            elif list1[i] < list2[i] :
                return 0xFF
            else : 
                return 0xF
        else : 
            #one is int and other is list or both are list 
            if type(list1[i]) == int :
                #print([list1[i]],list2[i])
                ans += compare_lists([list1[i]],list2[i])
            elif type(list2[i]) == int : 
                ans += compare_lists(list1[i],[list2[i]])
            else :
                ans += compare_lists(list1[i],list2[i])
            if ans  == 0xFF:
                return ans
            elif ans == 0xF : 
                return ans
    if len(list1) > len(list2) :
        return 0xF
    elif len(list1) == len(list2) :
        return ans
    else :
        return 0xFF
    
with open("input.txt", 'r') as f:
    raw_input = [x.replace("\n", "") for x in f.readlines()]
    arr_pairs = []
    for ele in raw_input : 
        if ele == "" : 
            continue
        arr_pairs.append(json.loads(ele))
    #print(arr_pairs)
    arr_pairs.extend([[[2]],[[6]]])
    print(arr_pairs)

    #bubble sort on arr_pairs
    swap = True
    for i in range(len(arr_pairs)-1) :
        if swap == False :
            break
        swap = False
        for j in range(len(arr_pairs)-1-i) :
            if compare_lists(arr_pairs[j],arr_pairs[j+1]) == 0xF :
                arr_pairs[j],arr_pairs[j+1] = arr_pairs[j+1],arr_pairs[j]
                swap = True
    print(arr_pairs)
    idx2 = -1
    idx6 = -1
    for i in range(len(arr_pairs)) :
        if arr_pairs[i] == [[2]] :
            idx2 = i
        if arr_pairs[i] == [[6]] :
            idx6 = i
            break 
    print(idx2,idx6)
    print((idx2+1)*(idx6+1))
    
    
