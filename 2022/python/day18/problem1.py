if __name__ == "__main__" :
    f=open("input.txt","r")
    cube_arr = [list(map(int,x.rstrip().split(","))) for x in f.readlines()]
    #print(cube_arr)
    #each cube surface area 6 minus any shared sides 
    sur_area = 0 
    for each_cube in cube_arr : 
        cube_area = 6 
        for x,y,z in cube_arr : 
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
    print(sur_area)
    
