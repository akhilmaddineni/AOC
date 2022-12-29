import re 
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])      
    
with open("input.txt", 'r') as f:
    raw_input = [x.replace("\n", "") for x in f.readlines()]
    sensor_pos = []
    beacon_pos = []
    for ele in raw_input: 
        x1,y1,x2,y2 = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", ele).groups()
        sensor_pos.append((int(x1),int(y1)))
        beacon_pos.append((int(x2),int(y2)))
    print(sensor_pos)
    print(beacon_pos)
    
    sensor_range = [] #sensor range co-ordinates 
    for i in range(len(sensor_pos)):
        m_dist = manhattan_distance(sensor_pos[i],beacon_pos[i])
        sensor_range.append(([sensor_pos[i][0]-m_dist,sensor_pos[i][1]], 
                             [sensor_pos[i][0]+m_dist,sensor_pos[i][1]], 
                             [sensor_pos[i][0],sensor_pos[i][1]-m_dist], 
                             [sensor_pos[i][0],sensor_pos[i][1]+m_dist]))
    #print(sensor_range)
    
    #on y axis get the range of x axis at same y
    y = 2000000 
    sensor_overlap = []
    for arr in sensor_range : 
        if y >= arr[2][1]  and y <= arr[3][1]  :
            #calculate the range of x axis at y 
            offset  = abs(y - arr[1][1])
            if offset != 0 :
                x_range = (arr[0][0]+offset, arr[1][0]-offset)
                sensor_overlap.append(x_range)
            else : 
                print("TODO : handle this case")
            
    sensor_overlap=sorted(sensor_overlap)            
    print(sensor_overlap)
    x = sensor_overlap[0][0]
    count = 0
    
    on_line = []
    
    for i in range(len(sensor_pos)) :
        if sensor_pos[i][1] == y : 
            on_line.append(sensor_pos[i])
        if beacon_pos[i][1] == y :
            on_line.append(beacon_pos[i])
    print(on_line)
    
    for i in range(len(sensor_overlap)) : 
        if x > sensor_overlap[i][1] :
            continue
        if x < sensor_overlap[i][0] :
            x = sensor_overlap[i][0]
        count += sensor_overlap[i][1] - x + 1
        x = sensor_overlap[i][1]+1
    count -= len(set(on_line))
    
    print(count)
    
    
    
# if __name__=="__main__" : 
#     p1 = [8,7]
#     p2 = [2,10]
#     m = manhattan_distance(p1,p2)
#     print(m)
#     import re

#     string = "Sensor at x=2, y=18: closest beacon is at x=-2, y=15"

#     # Use a regular expression to capture the x and y values
#     x1,y1,x2,y2 = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", string).groups()

#     print(x1,y1,x2,y2)

# TOO much memory with : 

    # min_x = min([x[0] for x in sensor_pos])
    # min_y = min([x[1] for x in sensor_pos])
    # max_x = max([x[0] for x in sensor_pos])
    # max_y = max([x[1] for x in sensor_pos])
    
    # min_x2 = min([x[0] for x in beacon_pos])
    # min_y2 = min([x[1] for x in beacon_pos])
    # max_x2 = max([x[0] for x in beacon_pos])
    # max_y2 = max([x[1] for x in beacon_pos])
    
    # min_x = min(min_x,min_x2)
    # min_y = min(min_y,min_y2)
    # max_x = max(max_x,max_x2)
    # max_y = max(max_y,max_y2)
    
    # #need to extend more to the left and right and up and down to handle the case where the sensor is at the edge
    # # min_x -= max(max_x,max_y)
    # # min_y -= max(max_x,max_y)
    # # max_x += max(max_x,max_y)
    # # max_y += max(max_x,max_y)
    
    # #create a grid 
    # grid = [["." for x in range(min_x,max_x+1)] for y in range(min_y,max_y+1)]
    
    # #fill in the sensor and beacon positions

    # for x,y in sensor_pos :
    #     grid[y - min_y][x - min_x] = "S"

    # for x,y in beacon_pos :
    #     grid[y - min_y][x - min_x] = "B"
        
    

    # #cal the manhattan distance between each sensor and beacon and fill the range char # in the grid
    # for i in range(len(sensor_pos)) : 
    #     m_dist = manhattan_distance(sensor_pos[i],beacon_pos[i])
    #     #fill right and left of the sensor pos with # for the manhattan distance
    #     for j in range(m_dist+1) :
    #         if grid[sensor_pos[i][1]- min_y][sensor_pos[i][0]-j-min_x] == "." :
    #             grid[sensor_pos[i][1]- min_y][sensor_pos[i][0]-j-min_x] = "#"
    #         if grid[sensor_pos[i][1]- min_y][sensor_pos[i][0]+j-min_x] == "." :
    #             grid[sensor_pos[i][1]- min_y][sensor_pos[i][0]+j-min_x] = "#"   
    #         for k in range(m_dist+1-j) :
    #             if grid[sensor_pos[i][1]-j-min_y][sensor_pos[i][0]-k-min_x] == "." :
    #                 grid[sensor_pos[i][1]-j-min_y][sensor_pos[i][0]-k-min_x] = "#"
    #             if grid[sensor_pos[i][1]-j-min_y][sensor_pos[i][0]+k-min_x] == "." :
    #                 grid[sensor_pos[i][1]-j-min_y][sensor_pos[i][0]+k-min_x] = "#"
    #             #fill down the pyramid with # for the manhattan distance
    #             if grid[sensor_pos[i][1]+j-min_y][sensor_pos[i][0]-k-min_x] == "." :
    #                 grid[sensor_pos[i][1]+j-min_y][sensor_pos[i][0]-k-min_x] = "#"
    #             if grid[sensor_pos[i][1]+j-min_y][sensor_pos[i][0]+k-min_x] == "." :
    #                 grid[sensor_pos[i][1]+j-min_y][sensor_pos[i][0]+k-min_x] = "#"
    # # for ele in grid : 
    # #     print(ele)
    
    # #find number of # in the grid at y = 2000000 
    # count = 0 
    # for i in range(len(grid[0])) : 
    #     if grid[2000000-min_y][i] == "#" : 
    #         count += 1
    # print(count)
        
        
        
    
