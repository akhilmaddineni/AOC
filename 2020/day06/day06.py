f=open("input.txt","r")
lines = f.readlines()

answers = [[]]

for line in lines : 
    line = line.strip().split(" ")
    #print(line)
    if len(line) == 1 and line[0] == '': 
        answers.append([])
    else :
        for ele in line :
            answers[-1].append(ele)

ans1 = 0 
ans2 = 0 

for answer in answers : 
    temp_set = set()
    temp_set2 = set(list("abcdefghijklmnopqrstuvwxyz"))
    for ele in answer :
        temp_set.update(set(list(ele)))
        temp_set2.intersection_update(set(list(ele)))
    ans1 += len(temp_set)
    ans2 += len(temp_set2)


print(ans1)
print(ans2)
