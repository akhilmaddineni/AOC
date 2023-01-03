
def flood_fill(grid, start, max_x, max_y, max_z):
    stack = [start]
    while stack:
        x, y, z = stack.pop()
        # Check if the current point is out of bounds or has already been visited
        if x < 0 or x >= max_x or y < 0 or y >= max_y or z < 0 or z >= max_z or grid[x][y][z] != 0:
            continue
        # Mark the current point as visited
        grid[x][y][z] = 1
        # Add the neighbors of the current point to the stack
        stack.extend([(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)])

    #GPT to scale up the floodfill to 3d !

if __name__ == "__main__" :
    f=open("input.txt","r")
    cube_arr = [tuple(map(int,x.rstrip().split(","))) for x in f.readlines()]
    print(cube_arr)
    #each cube surface area 6 minus any shared sides 
    sur_area = 0 
    max_xyz = 0
    for each_cube in cube_arr : 
        cube_area = 6 
        for x,y,z in cube_arr : 
            max_xyz = max(max_xyz,x,y,z)
            if (x,y) == (each_cube[0],each_cube[1]) : 
                if abs(z-each_cube[2]) ==1 : 
                    cube_area -=1
            elif (y,z) == (each_cube[1],each_cube[2]) : 
                if abs(x-each_cube[0]) ==1 : 
                    cube_area -=1
            elif (z,x) == (each_cube[2],each_cube[0]) : 
                if abs(y-each_cube[1]) ==1 : 
                    cube_area -=1
        if cube_area > 0 : 
            sur_area += cube_area
    
    print(max_xyz)
    #grid for flood fill 
    grid = [[[0 for x in range(max_xyz+1)] for y in range(max_xyz+1)] for z in range(max_xyz+1)]
    
    #fill grid with 1s for each cube
    for x,y,z in cube_arr : 
        grid[x][y][z] = 1
    
    flood_fill(grid, (0,0,0), max_xyz+1, max_xyz+1, max_xyz+1)
    unvisited = []
    count = 0
    for x in range(max_xyz+1):
        for y in range(max_xyz+1):
            for z in range(max_xyz+1):
                if grid[x][y][z] == 0:
                    count += 1
                    unvisited.append((x,y,z))
    #check if adjacent to any of the unvisited
    for each_cube in cube_arr :
        if (each_cube[0]+1,each_cube[1],each_cube[2]) in unvisited :
            sur_area -=1
        if (each_cube[0]-1,each_cube[1],each_cube[2]) in unvisited :
            sur_area -=1
        if (each_cube[0],each_cube[1]+1,each_cube[2]) in unvisited :
            sur_area -=1
        if (each_cube[0],each_cube[1]-1,each_cube[2]) in unvisited :
            sur_area -=1
        if (each_cube[0],each_cube[1],each_cube[2]+1) in unvisited :
            sur_area -=1
        if (each_cube[0],each_cube[1],each_cube[2]-1) in unvisited :
            sur_area -=1
    print(sur_area)
    
