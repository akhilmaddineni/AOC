from collections import deque
f=open("input.txt","r")
lines = f.readlines()
arr = []
for line in lines : 
    arr_num = [int(num) for num in line.strip()]
    arr.append(arr_num)

ans1 = 0 
max_x  = len(arr)
max_y = len(arr[0])

max_ele = 9
#append padding 
for i in range(max_x):
    arr[i] = [max_ele]+arr[i]+[max_ele]

arr = [[max_ele for _ in range(max_y+2)]]+arr+[[max_ele for _ in range(max_y+2)]]
    

for i in range(1,max_x+1):
    for j in range(1,max_y+1):
        if arr[i][j] < arr[i-1][j] and arr[i][j] < arr[i+1][j] and arr[i][j] < arr[i][j-1] and arr[i][j] < arr[i][j+1]:
            ans1 += arr[i][j]+1

print(f"part1 : {ans1}")

ans2 = 0 

#find number of blocks 
block_arr = []
for i in range(1,max_x+1):
    for j in range(1,max_y+1):
        if arr[i][j] != 9 : 
            temp_count = 0 
            queue = deque()
            queue.append((i,j))
            while queue :
                #print(queue)
                cur_point = queue.pop()
                temp_count += 1
                arr[cur_point[0]][cur_point[1]] = 9
                for off_i,off_j in [(-1,0),(1,0),(0,1),(0,-1)]:
                    if arr[cur_point[0]+off_i][cur_point[1]+off_j] != 9 :
                        if (cur_point[0]+off_i,cur_point[1]+off_j) not in queue:
                            queue.append((cur_point[0]+off_i,cur_point[1]+off_j))
            #print(temp_count)
            block_arr.append(temp_count)
#print(block_arr)
block_arr.sort()
print(f"part2 : {block_arr[-1]*block_arr[-2]*block_arr[-3]}")
