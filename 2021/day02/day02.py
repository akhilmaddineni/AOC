import sys
horizontal  = 0 
depth = 0
depth_1=0
aim = 0
f=open("input.txt","r")
lines = f.readlines()
for line in lines :
    instruction = line.rstrip().split(" ")
    if instruction[0] == "forward" :
        horizontal += int(instruction[1])
        depth += int(instruction[1])*aim
    elif instruction[0] == "down" :
        depth_1 += int(instruction[1])
        aim += int(instruction[1])
    elif instruction[0] == "up" :
        depth_1 -= int(instruction[1])
        aim -= int(instruction[1])
print(horizontal*depth_1)
print(horizontal*depth)