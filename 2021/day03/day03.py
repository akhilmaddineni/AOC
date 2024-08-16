f=open("input.txt","r")
lines = f.readlines()
hash_map = [{0:0,1:0} for _ in lines[0].rstrip()]
num_list = []
for line in lines :
    cur_num = line.rstrip()
    for i in range(len(cur_num)):
        hash_map[i][int(cur_num[i])] += 1
    num_list.append(cur_num)

num = ""
flip = "" 

for i in range(len(hash_map)) :
    bin_num = "0"
    if hash_map[i][0] < hash_map[i][1] :
        bin_num = "1"
    num+=bin_num
    flip += "1" if bin_num == "0" else "0"

num = int(num,2)
flip = int(flip,2)
print(f"ans1:{num*flip}")  

#########
o2_gen_rating = []
co2_gen_rating = []
start_num ="0"
if hash_map[0][0] <= hash_map[0][1]:
    start_num = "1"
for num in num_list:
    if num[0] == start_num :
        o2_gen_rating.append(num)
    else :
        co2_gen_rating.append(num)
idx=1 
#print(o2_gen_rating)
while len(o2_gen_rating)> 1: 
    num_0 = 0
    num_1 = 0
    num0_list = []
    num1_list = []
    for i in range(len(o2_gen_rating)):
        if o2_gen_rating[i][idx] == "0":
            num0_list.append(o2_gen_rating[i])
            num_0 += 1
        else :
            num1_list.append(o2_gen_rating[i])
            num_1 += 1
    if num_0 <= num_1 :
        o2_gen_rating = num1_list
    else :
        o2_gen_rating = num0_list
    idx+=1 
    #print(o2_gen_rating)
print(o2_gen_rating)

idx=1 
#print(co2_gen_rating)
while len(co2_gen_rating)> 1: 
    num_0 = 0
    num_1 = 0
    num0_list = []
    num1_list = []
    for i in range(len(co2_gen_rating)):
        if co2_gen_rating[i][idx] == "0":
            num0_list.append(co2_gen_rating[i])
            num_0 += 1
        else :
            num1_list.append(co2_gen_rating[i])
            num_1 += 1
    if num_0 <= num_1 :
        co2_gen_rating = num0_list
    else :
        co2_gen_rating = num1_list
    idx+=1 
    #print(co2_gen_rating)
print(co2_gen_rating)
print(int(o2_gen_rating[0],2)*int(co2_gen_rating[0],2))

