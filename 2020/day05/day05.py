import sys
f=open("input.txt","r")
lines = f.readlines()

ans1 = 0 
min_seat_num = sys.maxsize
seat_num_xor = 0
for line in lines : 
    boarding_pass = line.strip()
    left = 0 
    right = 127
    idx  = 0 
    mid = (left+right)//2
    #0-127
    while left < right and idx <7: 
        mid = (left+right)//2
        if boarding_pass[idx] == "F":
            right = mid 
        elif boarding_pass[idx] == "B":
            left = mid
        idx +=1
    if boarding_pass[6] == "B":
        row = mid+1
    else :
        row = mid  
    #0-7
    left = 0 
    right = 7 
    idx = 7 
    while left<right and idx <10:
        mid = (left+right)//2 
        if boarding_pass[idx] == "L":
            right = mid 
        elif boarding_pass[idx] == "R":
            left=mid
        idx+=1 
    if boarding_pass[-1] == "R":
        col = mid+1 
    else :
        col = mid
    #print(f"{row} {col}")
    ans1 = max(ans1,8*row+col)
    min_seat_num = min(min_seat_num,8*row+col)
    seat_num_xor ^= 8*row+col

    #print(ans1)
print(f"part1 : {ans1}")

for i in range(min_seat_num,ans1+1):
    seat_num_xor ^= i

print(f"part2 : {seat_num_xor}")

