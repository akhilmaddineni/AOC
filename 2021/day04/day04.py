f=open("input.txt","r")
lines = f.readlines()
numbers = [int(num) for num in lines[0].strip().split(",")]
bingo_arr = []
covered_arr = []
colcount_arr = []
for line in lines[1:]:
    if line.rstrip() == "":
        bingo_arr.append(dict())
        covered_arr.append([])
    else :
        bingo_arr[-1][tuple(int(num) for num in line.rstrip().split())] = 0

num_cols = len(lines[2].rstrip().split())
is_won = []
for i in range(len(bingo_arr)):
    colcount_arr.append([0 for _ in range(num_cols)])
    is_won.append(False)

for num in numbers : 
    i=0
    flag = False
    # print(num)
    for bingo in bingo_arr :
        if is_won[i] :
            i+=1
            continue
        for key in bingo.keys():
            if num in key :
                bingo[key] += 1
                covered_arr[i].append(num)
                col_idx = key.index(num)
                colcount_arr[i][col_idx] += 1
                if bingo[key] == 5 or colcount_arr[i][col_idx] == 5:
                    flag = True
                    is_won[i] = True
                    break
        if is_won[i] :
            sum_all = 0
            for key in bingo.keys():
                sum_all += sum(key)
            print((sum_all-sum(covered_arr[i]))*num)
        i+=1

    # if flag :
    #     break
print(colcount_arr)
#print(flag)
                    

