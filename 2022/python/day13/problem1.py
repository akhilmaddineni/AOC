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
    ans = 0
    for i in range(0,len(arr_pairs),2) : 
        arr1 = arr_pairs[i]
        arr2 = arr_pairs[i+1]
        if compare_lists(arr1,arr2) == 0xFF :
            print(arr1)
            print(arr2)
            print(i//2+1)
            ans += i//2+1
    print(ans)
    
