ans = 0 
with open("input.txt",'r') as f : 
    ip = [ x.replace('\n','') for x in f.readlines()]
    head = (0,0)
    tail = (0,0)
    tail_vis = set()
    tail_vis.add(tail)
    for line in ip :
        direction,length = line.split(" ")
        length = int(length)
        if direction == "L" :
            for i in range(length): 
                head=(head[0]-1,head[1])
                if head[1] == tail[1] :
                    if head[0]-tail[0]<-1 :
                        tail=(tail[0]-1,tail[1])
                        tail_vis.add(tail)
                else : 
                    if head[0]-tail[0]<-1 :
                        if head[1]>tail[1] :
                            tail=(tail[0]-1,tail[1]+1)
                        else :
                            tail=(tail[0]-1,tail[1]-1)
                        tail_vis.add(tail)

        elif direction == "R" : 
            for i in range(length) : 
                head=(head[0]+1,head[1])
                if head[1] == tail[1] :
                    if head[0]-tail[0]>1 :
                        tail=(tail[0]+1,tail[1])
                        tail_vis.add(tail)
                else :
                    if head[0]-tail[0]>1 :
                        if head[1]>tail[1] :
                            tail=(tail[0]+1,tail[1]+1)
                        else :
                            tail=(tail[0]+1,tail[1]-1)
                        tail_vis.add(tail)
        #up and down are tricky 
        elif direction == "U" :
            for i in range(length) : 
                head=(head[0],head[1]+1)
                #if x axis is same - no diagnol pass
                if head[0] == tail[0]:
                    if head[1]-tail[1]>1 :
                        tail=(tail[0],tail[1]+1)
                        tail_vis.add(tail)
                else : 
                    #diagnol pass
                   if head[1]-tail[1]>1 :
                        if head[0]>tail[0] :
                            tail=(tail[0]+1,tail[1]+1)
                        else :
                            tail=(tail[0]-1,tail[1]+1)
                        tail_vis.add(tail) 
        elif direction == "D" :
            for i in range(length) : 
                head=(head[0],head[1]-1)
                if head[0] == tail[0]:
                    if head[1]-tail[1]<-1 :
                        tail=(tail[0],tail[1]-1)
                        tail_vis.add(tail)
                else : 
                    if head[1]-tail[1]<-1 :
                        if head[0]>tail[0] :
                            tail=(tail[0]+1,tail[1]-1)
                        else :
                            tail=(tail[0]-1,tail[1]-1)
                        tail_vis.add(tail)
    #print(tail_vis)
    print(len(tail_vis))
                
        
    
        
             
