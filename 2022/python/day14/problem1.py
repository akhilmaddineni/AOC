import sys

def IsValid(grid, start_point, max_x, max_y):
    if start_point[0] > max_x or start_point[1] < 0 or start_point[1] > max_y :
        return False
    #already filled
    if grid[start_point[0]][start_point[1]] == 1 :
        return False
    if grid[start_point[0]][start_point[1]] == 2 :
        return False
    #below is stable
    if (grid[start_point[0]+1][start_point[1]+1] in (1,2) and grid[start_point[0]+1][start_point[1]-1] in (1,2) and grid[start_point[0]+1][start_point[1]] in (1,2)):
        return True
    return False

def GoDiagonalLeft(grid, start_point):
    if (grid[start_point[0]][start_point[1]] in (1,2)) and grid[start_point[0]][start_point[1]-1] == 0:
        return True
    return False

def GoDiagonalRight(grid, start_point):
    if (grid[start_point[0]][start_point[1]] in (1,2)) and grid[start_point[0]][start_point[1]+1] == 0:
        return True
    return False
        
def fill2(grid,start_point,max_x,max_y):
    flag = True
    #tbh this bug made me cry
    max_x,max_y=max_y,max_x
    while flag :
        #flag will be false if no more water can be filled
        flag = False
        y_pos = start_point[1]
        x_pos = start_point[0]
        while x_pos >= 0 and x_pos < max_x and grid[x_pos][y_pos] == 0:
            x_pos += 1
        x_pos -=1
        if IsValid(grid, [x_pos,y_pos], max_x, max_y) :
            grid[x_pos][y_pos] = 2
            flag = True
        else :
            while x_pos < max_x :
                if IsValid(grid,[x_pos,y_pos],max_x,max_y) :
                    grid[x_pos][y_pos] = 2
                    flag=True
                    break
                
                if GoDiagonalLeft(grid, [x_pos,y_pos]) :
                    if IsValid(grid,[x_pos,y_pos-1],max_x,max_y) :
                        grid[x_pos][y_pos-1] = 2
                        flag = True
                        break
                    else :
                        if y_pos-1 >=0 :
                            if grid[x_pos][y_pos-1] == 0:
                                y_pos = y_pos-1
                            else :
                                break
                        else :
                            break
                if GoDiagonalRight(grid, [x_pos,y_pos]) :
                    if IsValid(grid, [x_pos, y_pos + 1], max_x, max_y):
                        grid[x_pos][y_pos+1] = 2
                        flag = True
                        break
                    else :
                        if y_pos+1 <= max_y :
                            if grid[x_pos][y_pos + 1] == 0:
                                y_pos = y_pos + 1
                            else :
                                break
                        else :
                            break
                x_pos = x_pos + 1
                if (grid[x_pos][y_pos-1] in (1, 2) and grid[x_pos][y_pos] in (1, 2) and grid[x_pos][y_pos+1] in (1, 2)):
                    break            
    
with open("input.txt", 'r') as f:
    raw_input = [x.replace("\n", "") for x in f.readlines()]
    #finding bounds of the grid
    max_x = 0
    min_x = sys.maxsize
    max_y = 0
    rocks_list_all = []
    #each rock formation 
    for rocks in raw_input : 
        rocks_list_str = rocks.split("->")
        rocks_list_str = [x.strip() for x in rocks_list_str]
        #coordinates of rock formation 
        rocks_list = [x.split(',') for x in rocks_list_str]
        for i in range(len(rocks_list)) :
            rocks_list[i] = [int(x) for x in rocks_list[i]]
            max_x = max(max_x,rocks_list[i][0])
            min_x = min(min_x,rocks_list[i][0])
            max_y = max(max_y,rocks_list[i][1])
        rocks_list_all.append(rocks_list)
    
    #offset x axis 
    for rocks_list in rocks_list_all :
        for i in range(len(rocks_list)) :
            rocks_list[i][0] -= min_x
    max_x -= min_x
    #print(rocks_list_all)
    
    
    #grid
    grid = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
    
    #1 for rock formation and 2 for sand 
    #fill the grid with rock formation
    for i in range(len(rocks_list_all)) :
        rocks_list = rocks_list_all[i]
        for j in range(len(rocks_list)-1) : 
            #traverse the grid and fill the rock formation
            if rocks_list[j][0] == rocks_list[j+1][0] :
                #vertical line
                if rocks_list[j][1] < rocks_list[j+1][1] :
                    for k in range(rocks_list[j][1],rocks_list[j+1][1]+1) :
                        grid[k][rocks_list[j][0]] = 1
                else : 
                    for k in range(rocks_list[j+1][1],rocks_list[j][1]+1) :
                        grid[k][rocks_list[j][0]] = 1
            else :
                #horizontal line
                if rocks_list[j][0] < rocks_list[j+1][0] :
                    for k in range(rocks_list[j][0],rocks_list[j+1][0]+1) :
                        grid[rocks_list[j][1]][k] = 1
                else :
                    for k in range(rocks_list[j+1][0],rocks_list[j][0]+1) :
                        grid[rocks_list[j][1]][k] = 1
    
    #print grid 
    for ele in grid : 
        print(ele)
    
    start_point = [0,500-min_x]
    fill2(grid, start_point, max_x, max_y)
    # #flood fill 
    print("After flood fill")
    ans  = 0
    for ele in grid : 
        print(ele)
        ans += ele.count(2)
    print(ans)
        
        
    
