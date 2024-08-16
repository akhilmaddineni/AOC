f=open("input.txt","r")
lines = f.readlines()
numbers = lines[0].rstrip().split(",")
bingo_arr = []
covered_arr = []
for line in lines[1:]:
    if line.rstrip() == "":
        bingo_arr.append(dict())
        covered_arr.append([])
    else :
        bingo_arr[-1][tuple(int(num) for num in line.rstrip().split())] = 0

for num in numbers : 
    i=0
    flag = False
    for bingo in bingo_arr :
        for key in bingo.keys():
            if num in key :
                bingo[key] += 1
                covered_arr[i].append(num)
                if bingo[key] == 5 :
                    flag = True
                    break
        if flag :
            sum_all = 0
            for key in bingo.keys():
                sum_all += sum(key)
            print((sum_all-sum(covered_arr[i]))*num)
        i+=1
    if flag :
        break
                    

