import sys
from collections import deque
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

window = deque()
pre_sum = -1
for line in lines : 
    cur_num = int(line.rstrip())
    if len(window) < 3 : 
        window.append(cur_num)
    else: 
        if pre_sum == -1 : 
            pre_sum = sum(window)
        window.popleft()
        window.append(cur_num)
        cur_sum = sum(window)
        if pre_sum < cur_sum :
            ans2+=1
        pre_sum=cur_sum

print(ans2)

             
