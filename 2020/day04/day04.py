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
passports_dict = [{}]

need_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for line in lines : 
    line = line.strip().split(" ")
    #print(line)
    if len(line) == 1 and line[0] == '': 
        passports.append([])
        passports_dict.append({})
        continue
    else :
        for ele in line :
            #print(ele)
            key,val=ele.split(":")
            passports[-1].append(key)
            passports_dict[-1][key] = val
#print(len(passports))
print(passports_dict)


"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


ans1 = 0 
ans2 = 0
for passport in passports_dict :
    flag = True 
    flag_valid_val = True
    for key in need_keys :
        if not flag_valid_val :
            break
        if key not in passport :
            flag = False
            #print(passport)
            break
        else : 
            if key == 'byr' : 
                if not (len(passport[key]) == 4 and passport[key].isdigit()):
                    flag_valid_val = False
                    break
                year = int(passport[key])
                if year < 1920 or year > 2002 : 
                    flag_valid_val = False
                    break
            elif key == 'iyr':
                if not (len(passport[key]) == 4 and passport[key].isdigit()):
                    flag_valid_val = False
                    break
                year = int(passport[key])
                if year < 2010 or year > 2020 : 
                    flag_valid_val = False
                    break
            elif key == 'eyr':
                if not (len(passport[key]) == 4 and passport[key].isdigit()):
                    flag_valid_val = False
                    break
                year = int(passport[key])
                if year < 2020 or year > 2030 : 
                    flag_valid_val = False
                    break
            elif key == 'hgt':
                if passport[key][-2:] == 'cm':
                    val = int(passport[key][:-2])
                    if val < 150 or val > 193 : 
                        flag_valid_val = False
                        break
                elif passport[key][-2:] == 'in':
                    val = int(passport[key][:-2])
                    if val < 59 or val > 76 : 
                        flag_valid_val = False
                        break
                else :
                    flag_valid_val = False
                    break

            elif key == 'hcl':
                if not(passport[key][0] == '#' and len(passport[key]) ==7) : 
                    flag_valid_val = False
                    break 
                else : 
                    for char in passport[key][1:]:
                        if char not in "0123456789abcdef":
                            flag_valid_val = False
                            break
            elif key == 'ecl' : 
                if passport[key] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): 
                    flag_valid_val = False
                    break
            elif key == 'pid': 
                if not (len(passport[key]) == 9 and passport[key].isdigit()):
                    flag_valid_val = False
                    break
    if flag : 
        ans1+=1
        if flag_valid_val :
            ans2 += 1
print(ans1)
print(ans2)

