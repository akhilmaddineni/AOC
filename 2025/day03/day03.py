ans = 0 
with open("input.txt") as f:
    for line in f:
        int_num = [int(x) for x in line.rstrip()]
        #print(int_num)
        max_right = max(int_num)
        max_left  = 0
        cur_max  = max_left*10 + max_right
        for i in range(len(int_num)-1):
            max_left = max(max_left, int_num[i])
            max_right = max(int_num[i+1:])
            candidate = max_left*10 + max_right
            if candidate > cur_max:
                cur_max = candidate
            # else :
            #     break
        #print(cur_max)
        ans += cur_max
print(ans)
