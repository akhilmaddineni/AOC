"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

"""

f=open("input.txt","r")
lines = f.readlines()

passports = [[]]

need_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for line in lines : 
    line = line.strip().split(" ")
    #print(line)
    if len(line) == 1 : 
        passports.append([])
        continue
    else :
        for ele in line :
            #print(ele)
            key,val=ele.split(":")
            passports[-1].append(key)
print(passports)

ans1 = 0 
for passport in passports :
    flag = True 
    for key in need_keys :
        if key not in passport :
            flag = False
            break
    if flag : 
        ans1+=1

print(ans1)

