#TODO : implement with some sort of tree/sort while parsing the input (more efficient?)
ans =0
with open("input.txt",'r') as f : 
    matrix = [ list(map(int , list(x.replace('\n','')))) for x in f.readlines()]
    #print(matrix)
    #flag matrices - rows and columns (left to right and vice versa)
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    count_row_left  = [[0]*num_cols for _ in range(num_rows)]
    count_row_right = [[0]*num_cols for _ in range(num_rows)]
    count_col_top  = [[0]*num_cols for _ in range(num_rows)]
    count_col_bot = [[0]*num_cols for _ in range(num_rows)]

    #create row counts
    for i in range(num_rows) : 
        if i == 0 or i == num_rows-1 :
            #top and bottom rows are always 0 
            continue
        for j in range(1,num_cols) : 
            #all are true by default no need to check for 0/-1
            if j != num_cols-1 :
                #store number of adjecent cells that are smaller than current cell
                if j ==1 : 
                    count_row_left[i][j] = 1
                    count_row_right[i][-j-1] = 1
                else :
                    if matrix[i][j]>matrix[i][j-1] :
                        #loop again - not efficient solution
                        for k in range(j-1,-1,-1) :
                            if matrix[i][j]>matrix[i][k] :
                                count_row_left[i][j] += 1
                            else :
                                count_row_left[i][j] += 1
                                break
                    else :
                        count_row_left[i][j] = 1
                    if matrix[i][-j-1]>matrix[i][-j] :
                        for k in range(-j,0,1) :
                            if matrix[i][-j-1]>matrix[i][k] :
                                count_row_right[i][-j-1] += 1
                            else :
                                count_row_right[i][-j-1] += 1
                                break
                        #count_row_right[i][-j-1] = count_row_right[i][-j] + 1
                    else :
                        count_row_right[i][-j-1] = 1
    
    #print(count_row_left)
    #print(count_row_right)

    #create col counts
    for j in range(num_cols) :
        if j == 0 or j == num_cols-1 :
            #edges
            continue
        for i in range(1,num_rows) :
            if i != num_rows-1 :
                if i == 1 :
                    count_col_top[i][j] = 1
                    count_col_bot[-i-1][j] = 1
                else :
                    if matrix[i][j]>matrix[i-1][j] :
                        for k in range(i-1,-1,-1) :
                            if matrix[i][j]>matrix[k][j] :
                                count_col_top[i][j] += 1
                            else :
                                count_col_top[i][j] += 1
                                break
                    else :
                        count_col_top[i][j] = 1
                    if matrix[-i-1][j]>matrix[-i][j] :
                        for k in range(-i,0,1) :
                            if matrix[-i-1][j]>matrix[k][j] :
                                count_col_bot[-i-1][j] += 1
                            else :
                                count_col_bot[-i-1][j] += 1
                                break
                    else :
                        count_col_bot[-i-1][j] = 1
    #print(count_col_top)
    #print(count_col_bot)

    for i in range(1,num_rows-1) :
        for j in range(1,num_cols-1) :
            ans = max(ans,count_row_left[i][j]*count_row_right[i][j]*count_col_top[i][j]*count_col_bot[i][j])
    print(ans)
        
    
        
             
