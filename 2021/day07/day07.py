import sys
f=open("input.txt","r")
lines = f.readlines()
numbers=[int(num) for num in lines[0].strip().split(',')]
numbers.sort()
n=len(numbers)

if n%2 == 0 : 
    median = (numbers[n//2 -1 ]+numbers[n//2])//2
else :
    median = numbers[n//2]

ans = 0 
for num in numbers :
    ans += abs(num-median)

print(f"part 1 : {ans}")

def caluculate_fuel_consumed(cur_num):
    cur_sum = 0 
    for num in numbers:
        diff = abs(cur_num-num)
        cur_sum += (diff*(diff+1))//2
    return cur_sum

ans2 = sys.maxsize

#find min sum 

min_num = min(numbers)
max_num = max(numbers)
for num in range(min_num,max_num+1):
    ans2 = min(ans2,caluculate_fuel_consumed(num))
print(f"part2 : {ans2}")
