from collections import defaultdict
f=open("input.txt","r")
lines = f.readlines()
states=[int(num) for num in lines[0].strip().split(",")]
print(states)
count_dict = defaultdict(int)
for i in range(9):
    count_dict[i] = 0 
for i in states:
    count_dict[i] += 1 

for i in range(256):
    new_entries = count_dict[0]
    for j in range(1,9):
        count_dict[j-1]=count_dict[j]
    count_dict[8]=new_entries #new fish
    count_dict[6]+=new_entries #resets from 0 to 6
print(sum(count_dict.values()))
