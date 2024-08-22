from collections import deque
f=open("input.txt","r")
lines = f.readlines()

map_symbol = {
    ')' : '(', 
    ']' : '[',
    '}' : '{', 
    '>' : '<'
}

map_key = {
    '(' : ')', 
    '[' : ']',
    '{' : '}', 
    '<' : '>'
}


value = {
    ')' : 3,
    ']' : 57, 
    '}' : 1197,
    '>' : 25137
}

value_ele = {
    ')' : 1,
    ']' : 2, 
    '}' : 3,
    '>' : 4
}

ans1 = 0 

autocomplete_score_arr = []
for line in lines : 
    queue = deque()
    line = line.strip()
    count = 0 
    flag = True
    for ele in line :
        if ele in map_symbol: 
            last_ele = queue.pop()
            if last_ele != map_symbol[ele] : 
                print(ele)
                ans1 += value[ele]
                flag = False
                break
                #print(f"{last_ele} {ele}")
                
        else :
            queue.append(ele)
    if flag:
        cur_val = 0 
        while queue :
            cur_val *= 5 
            cur_ele = queue.pop()
            cur_val += value_ele[map_key[cur_ele]]
        autocomplete_score_arr.append(cur_val)


print(f"part 1 : {ans1}")

autocomplete_score_arr.sort()
print(f"part2 : {autocomplete_score_arr[len(autocomplete_score_arr)//2  ]}")

