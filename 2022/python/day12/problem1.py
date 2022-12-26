
class Item:
    def __init__(self,row,col,dist):
        self.row = row
        self.col = col
        self.dist = dist

#BFS to find the shortest path from source to destination
def isValid(matrix,visited,i,j,s_i,s_j) : 

    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or visited[i][j] == True  :
        return False
    if (matrix[s_i][s_j] == "S" and matrix[i][j] not in ("a","b") ) :
        return  False
    if (matrix[i][j] == "E" and matrix[s_i][s_j] not in ("y","z") ) :
        return False
    if (matrix[s_i][s_j] == "S" and matrix[i][j] in ("a", "b")) or (matrix[i][j] == "E" and matrix[s_i][s_j] in ("y","z") ) or ord(matrix[i][j]) - ord(matrix[s_i][s_j]) <= 1:
        return True
    return False


def shortest_path(matrix) :
    s = Item(0,0,0)
    for i in range(len(matrix)) : 
        for j in range(len(matrix[0])) : 
            if matrix[i][j] == "S" :
                s = Item(i,j,0)
                break
    vis = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
    
    q = []
    q.append(s)
    vis[s.row][s.col] = True
    
    while len(q) != 0 : 
        s = q.pop(0)
        print(s.row,s.col,s.dist)

        if matrix[s.row][s.col] == "E" :
            return s.dist
        #up
        if isValid(matrix,vis,s.row+1,s.col,s.row,s.col) and not vis[s.row+1][s.col] :
            q.append(Item(s.row+1,s.col,s.dist+1))
            vis[s.row+1][s.col] = True
        #down
        if isValid(matrix,vis,s.row-1,s.col,s.row,s.col) :
            q.append(Item(s.row-1,s.col,s.dist+1))
            vis[s.row-1][s.col] = True
        #left
        if isValid(matrix,vis,s.row,s.col-1,s.row,s.col) :
            q.append(Item(s.row,s.col-1,s.dist+1))
            vis[s.row][s.col-1] = True
        #right
        if isValid(matrix,vis,s.row,s.col+1,s.row,s.col) :
            q.append(Item(s.row,s.col+1,s.dist+1))
            vis[s.row][s.col+1] = True
    return -1


with open("input.txt",'r') as f : 
    raw_input = [x.replace("\n","") for x in f.readlines()]
    matrix = [[e for e in x] for x in raw_input]
    # for ele in matrix:
    #     print(ele)
    print(shortest_path(matrix))



    
    
    
            
