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
    
    #part 2 
    for y in range(0,4000000) :
        #on y axis get the range of x axis at same y
        #y = 10 
        sensor_overlap = []
        for arr in sensor_range : 
            if y >= arr[2][1]  and y <= arr[3][1]  :
                #calculate the range of x axis at y 
                offset  = abs(y - arr[1][1])
                x_range = (arr[0][0]+offset, arr[1][0]-offset)
                sensor_overlap.append(x_range)

        if sensor_overlap == [] :
            continue     
        sensor_overlap=sorted(sensor_overlap)            
        #print(sensor_overlap)
        x = sensor_overlap[0][0]

        #print(on_line)
        
        coordinates =(-1,-1)
        
        for i in range(len(sensor_overlap)) : 
            if x > sensor_overlap[i][1] :
                continue
            if x < sensor_overlap[i][0] :
                #x = sensor_overlap[i][0]
                coordinates = (sensor_overlap[i][0]-1,y)
                break 
            #count += sensor_overlap[i][1] - x + 1
            x = sensor_overlap[i][1]+1
        if coordinates != (-1,-1) :
            print(f"for y = {y} coordinates = {coordinates}")
            print(f"tune freq = {coordinates[0]*4000000 + coordinates[1]}")
            break 
        
    
