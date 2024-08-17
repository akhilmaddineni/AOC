f=open("input.txt","r")
lines = f.readlines()
points = []
max_x = -1
max_y = -1
for line in lines :
    point = line.strip().split("->")
    point = ([int(num) for num in point[0].strip().split(",")],[int(num) for num in point[1].strip().split(",")])
    max_x = max(max_x,point[0][0],point[1][0])
    max_y = max(max_y,point[0][1],point[1][1])
    
    
    if point[0][0] == point[1][0] or point[0][1] == point[1][1] :
        points.append(point)
    #this is for part2
    else : 
        slope  = (point[0][1]-point[1][1])//(point[0][0]-point[1][0])
        if slope == 1 or slope == -1 : 
            points.append(point)
#print(points)

arr = []
for i in range(max_x+1):
    arr.append([0 for _ in range(max_y+1)])

for point in points : 
    if point[0][0] == point[1][0] : 
        if point[0][1] <= point[1][1] : 
            for j in range(point[0][1],point[1][1]+1) : 
                arr[point[0][0]][j] += 1 
        else : 
            for j in range(point[1][1],point[0][1]+1) : 
                arr[point[0][0]][j] += 1 
    elif point[0][1] == point[1][1] : 
        if point[0][0] <= point[1][0] :
            for i in range(point[0][0],point[1][0]+1): 
                arr[i][point[0][1]] += 1
        else : 
            for i in range(point[1][0],point[0][0]+1): 
                arr[i][point[0][1]] += 1
    else : 
        # slope = (point[1][1]-point[0][1])//(point[1][0]-point[0][0])
        # if slope == 1 : 
        #     diff = abs(point[1][0]-point[0][0])
        #     if point[0][0] < point[1][0] and point[0][1] < point[1][1] :
        #         for i in range(diff+1):
        #             arr[point[0][0]+i][point[0][1]+i] += 1
        #     else : 
        #         for i in range(diff+1):
        #             arr[point[1][0]+i][point[1][1]+i] += 1
        # elif slope == -1 :
        #     diff = abs(point[1][0]-point[0][0])
        #     if point[0][0] > point[1][0] and point[0][1] > point[1][1]:
        #         for i in range(diff+1):
        #             arr[point[0][0]-i][point[0][1]-i] += 1
        #     else : 
        #         for i in range(diff+1):
        #             arr[point[1][0]-i][point[1][1]-i] += 1
        x_step = 1 if point[1][0] > point[0][0] else -1 
        y_step = 1 if point[1][1] > point[0][1] else -1 
        arr[point[0][0]][point[0][1]] += 1
        arr[point[1][0]][point[1][1]] += 1
        x,y = point[0][0]+x_step,point[0][1]+y_step
        while (x!=point[1][0]) and (y!=point[1][1]):
            arr[x][y] += 1
            x+=x_step
            y+=y_step

# for ele in arr:
#     print(ele)
ans1 = 0 
for i in range(max_x+1):
    for j in range(max_y+1):
        if arr[i][j] > 1 :
            ans1 += 1
print(ans1)
