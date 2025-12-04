def problem2(arr, num_selected):
    n = len(arr)
    dp = [[-1]*(num_selected+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1, n+1):
        for j in range(1, min(i, num_selected)+1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]*10 + arr[i-1])
    return dp[n][num_selected]



ans = 0 
ans2=0
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
        ans2 += problem2(int_num, 12)
print(ans)
print(ans2)
