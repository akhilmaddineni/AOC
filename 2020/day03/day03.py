f=open("input.txt","r")
lines = f.readlines()

grid = []
for line in lines : 
    grid.append(line.strip())

num_rows = len(grid)
num_cols = len(grid[0])

#move is right3 down 1 
x=0
y=0
ans1=0
while x < num_rows : 
    x+=1
    y+=3
    if grid[x%num_rows][y%num_cols] == '#':
        ans1+=1
print(f"part1 : {ans1}")

ans2 = ans1 #already covered right3 down 1
#need to cover r1,d1 , r5,d1 , r7,d1, r1,d2 
instructions = [(1,1),(5,1),(7,1),(1,2)]

for off_y,off_x in instructions:
    x=0
    y=0
    temp_ans=0
    while x < num_rows : 
        x+=off_x
        y+=off_y
        if x<num_rows:
            if grid[x%num_rows][y%num_cols] == '#':
                temp_ans+=1
    print(temp_ans)     
    ans2 *= temp_ans

print(f"part2 : {ans2}")

