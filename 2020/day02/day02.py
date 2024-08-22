f=open("input.txt","r")
lines = f.readlines()

ans1 = 0
ans2 = 0 
for line in lines : 
    instruction = line.strip().split(" ")
    range_valid = instruction[0].split("-")
    range_valid = (int(range_valid[0]),int(range_valid[1]))
    policy = instruction[1][0]
    count = instruction[2].count(policy)
    if count>=range_valid[0] and count<=range_valid[1]:
        ans1 += 1
    if (instruction[2][range_valid[0]-1] == policy or instruction[2][range_valid[1]-1] == policy) and instruction[2][range_valid[0]-1] != instruction[2][range_valid[1]-1] :
        ans2 += 1 
print(f"part1 : {ans1}")
print(f"part2 : {ans2}")