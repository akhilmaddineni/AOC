 
with open("input_p1.txt",'r') as f : 
    matrix = [ list(map(int , list(x.replace('\n','')))) for x in f.readlines()]
    #print(matrix)
    #flag matrices - rows and columns (left to right and vice versa)
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    flag_row_left  = [[True]*num_cols for _ in range(num_rows)]
    flag_row_right = [[True]*num_cols for _ in range(num_rows)]
    flag_col_top  = [[True]*num_cols for _ in range(num_rows)]
    flag_col_bot = [[True]*num_cols for _ in range(num_rows)]

    #create row flag masks
    for i in range(num_rows) : 
        if i == 0 or i == num_rows-1 :
            #top and bottom rows are always true 
            continue
        max_left = matrix[i][0]
        max_right = matrix[i][-1]
        for j in range(1,num_cols) : 
            #all are true by default no need to check for 0/-1
            if j != num_cols-1 :
                if matrix[i][j]<=max_left :
                    flag_row_left[i][j] = False
                else :
                    max_left=matrix[i][j]
                if matrix[i][-j-1]<=max_right :
                    flag_row_right[i][-j-1] = False
                else : 
                    max_right = matrix[i][-j-1]
    
    #print(flag_row_left)
    #print(flag_row_right)
    
    #create col flag masks 
    for j in range(num_cols) : 
        if j == 0 or j == num_cols - 1 :
            #edges
            continue
        max_top = matrix[0][j]
        max_bottom = matrix[-1][j]  
        for i in range(1,num_rows) : 
            if i != num_rows-1 : 
                if matrix[i][j]<=max_top :
                    flag_col_top[i][j]=False
                else : 
                    max_top=matrix[i][j]
                if matrix[-i-1][j]<=max_bottom : 
                    flag_col_bot[-i-1][j] = False
                else : 
                    max_bottom=matrix[-i-1][j]
    #print(flag_col_top)
    #print(flag_col_bot)
    count = 0 
    for i in range(num_rows) : 
        for j in range(num_cols) :
            if flag_row_left[i][j] or flag_row_right[i][j] or flag_col_top[i][j] or flag_col_bot[i][j] :
                count +=1
    print(count)
                
        
    
        
             
