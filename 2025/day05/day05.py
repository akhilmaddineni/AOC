ans = 0 
ans2=0

with open("input.txt") as f:
    ranges = []
    flag = False
    available_nums = set()
    for line in f: 
        line = line.rstrip()
        if line == "":
            flag = True
            continue
        if not flag:
            a, b = line.split("-")
            ranges.append( (int(a), int(b)) )
        elif line != "":
            available_nums.add(int(line))
    for num in available_nums:
        for a, b in ranges:
            if a <= num <= b:
                ans += 1
                break
    #check if ranges overlap and merge them
    ranges.sort()
    merged_ranges = []
    cur_a, cur_b = ranges[0]
    for a, b in ranges[1:]:
        if a <= cur_b:
            cur_b = max(cur_b, b)
        else:
            merged_ranges.append( (cur_a, cur_b) )
            cur_a, cur_b = a, b
    merged_ranges.append( (cur_a, cur_b) )
    for a, b in merged_ranges:
        ans2 += b - a + 1
print(ans)
print(ans2)
