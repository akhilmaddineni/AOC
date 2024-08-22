from collections import deque
f=open("input.txt","r")
lines = f.readlines()
arr = []
for line in lines : 
    line = [int(num) for num in line.strip()]
    arr.append(line)

print(arr)
num_rows = len(arr)
num_cols = len(arr[0])
#num of steps to run sim 
num_steps = 1000
directions = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,1),(1,-1)]
ans1 = 0 
for x_step in range(num_steps):
    extra_actiavations = deque()
    temp_act = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if arr[i][j] == 9 : 
                extra_actiavations.append((i,j))
                arr[i][j] = 0 
                ans1 += 1
                temp_act += 1 
            else :
                arr[i][j] += 1
    while extra_actiavations:
        cur_point = extra_actiavations.pop()
        for x,y in directions: 
            cur_x = cur_point[0]+x
            cur_y = cur_point[1]+y
            if cur_x>=0 and cur_x<num_rows and cur_y>=0 and cur_y<num_cols : 
                if arr[cur_x][cur_y] != 0 : 
                    if arr[cur_x][cur_y] == 9 : 
                        extra_actiavations.append((cur_x,cur_y))
                        ans1+=1
                        arr[cur_x][cur_y] = 0 
                        temp_act += 1
                    else : 
                        arr[cur_x][cur_y] += 1
    if temp_act == num_rows*num_cols: 
        print(f"found all activations at step : {x_step+1}")
        break


print(f"part1 : {ans1}")
