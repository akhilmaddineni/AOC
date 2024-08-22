f=open("input.txt","r")
lines = f.readlines()
arr = []
for line in lines :
    arr.append(int(line.strip()))

# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)): 
#         if arr[i]+arr[j] == 2020 :
#             print(f"{arr[i]*arr[j]}")
#             break

hash = {}
for num in arr : 
    if num in hash : 
        print(f"part1 : {num*hash[num]}")
        break
    else:
        hash[2020-num] = num

arr.sort()
i=0 
while i < len(arr)-2 :
    left = i+1
    right = len(arr)-1 
    while left < right : 
        if arr[i]+arr[left]+arr[right] == 2020 : 
            print(f"{arr[i]*arr[left]*arr[right]}")
            left += 1
            right -= 1
        elif arr[i]+arr[left]+arr[right] < 2020:
            left += 1
        else :
            right -= 1
    i+=1 


