"""
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
#.........................
#.............###.........
#............#...#........
.#..........#.....#.......
..#..........#.....#......
...#........#.......#.....
....#......s.........#....
.....#..............#.....
......#............#......
.......#..........#.......
........#........#........
.........########.........
"""

ans = 0 

def caluclate_tail_loc(head,tail) : 
    if head == tail :
        return tail
    else :
        #if x axis same , move up or down 
        if head[0] == tail[0] :
            if head[1]>tail[1] :
                if head[1]-tail[1]>1 :
                    tail = (tail[0],tail[1]+1)
            else :
                if head[1]-tail[1]<-1 :
                    tail = (tail[0],tail[1]-1) 
        #if y axis same , move left or right
        elif head[1] == tail[1] :
            if head[0]>tail[0] :
                if head[0]-tail[0]>1 :
                    tail = (tail[0]+1,tail[1])
            else :
                if head[0]-tail[0]<-1 :
                    tail = (tail[0]-1,tail[1])
        #if x and y axis are different , move diagnol
        else :
            if head[0]-tail[0]>1 :
                if head[1]>tail[1] :
                    tail=(tail[0]+1,tail[1]+1)
                else :
                    tail=(tail[0]+1,tail[1]-1)
            elif head[0]-tail[0]<-1 :
                if head[1]>tail[1] :
                    tail=(tail[0]-1,tail[1]+1)
                else :
                    tail=(tail[0]-1,tail[1]-1)
            elif head[1]-tail[1]>1 :
                if head[0]>tail[0] :
                    tail=(tail[0]+1,tail[1]+1)
                else :
                    tail=(tail[0]-1,tail[1]+1)
            elif head[1]-tail[1]<-1 :
                if head[0]>tail[0] :
                    tail=(tail[0]+1,tail[1]-1)
                else :
                    tail=(tail[0]-1,tail[1]-1)
        return tail


with open("input.txt",'r') as f : 
    ip = [ x.replace('\n','') for x in f.readlines()]
    #head = (0,0)
    tail = [(0,0) for _ in range(10)]
    #print(tail)
    tail_vis = set()
    tail_vis.add(tail[-1])
    for line in ip :
        direction,length = line.split(" ")
        length = int(length)
        if direction == "L" :
            for i in range(length): 
                tail[0]=(tail[0][0]-1,tail[0][1])
                for j in range(1,10) :
                    tail[j]=caluclate_tail_loc(tail[j-1],tail[j])
                tail_vis.add(tail[-1])

        elif direction == "R" : 
            for i in range(length) : 
                tail[0]=(tail[0][0]+1,tail[0][1])
                for j in range(1,10) :
                    tail[j]=caluclate_tail_loc(tail[j-1],tail[j])
                tail_vis.add(tail[-1])
        #up and down are tricky 
        elif direction == "U" :
            for i in range(length) : 
                tail[0]=(tail[0][0],tail[0][1]+1)

                for j in range(1,10) :
                    tail[j]=caluclate_tail_loc(tail[j-1],tail[j])
                tail_vis.add(tail[-1])
        elif direction == "D" :
            for i in range(length) : 
                tail[0]=(tail[0][0],tail[0][1]-1)
                for j in range(1,10) :
                    tail[j]=caluclate_tail_loc(tail[j-1],tail[j])
                tail_vis.add(tail[-1])
    #print(sorted(tail_vis))
    print(len(tail_vis))

                
        
    
        
             
