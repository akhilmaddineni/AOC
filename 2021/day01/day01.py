import sys
ans1  = 0 
prev_max = sys.maxsize
prev_max_slide = sys.maxsize
ans2 = 0
f=open("input.txt","r")
lines = f.readlines()
for line in lines :
    cur_num = int(line.rstrip())
    if prev_max <cur_num:
        ans1+=1 
    prev_max = cur_num
print(ans1)
print(ans2)

             
