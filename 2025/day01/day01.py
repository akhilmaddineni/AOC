ans = 0  # Count when landing exactly on 0
ans2 = 0  # Count all times passing through 0
pos = 50

with open("input.txt", 'r') as f:
    for line in f:
        line = line.rstrip()
        direction = line[0]
        num = int(line[1:])
        orig_pos = pos
        
        if direction == "L":
            new_pos = pos - num
            # Count how many times we pass through 0 going left
            if orig_pos > 0 and new_pos <= 0:
                # We crossed from positive to 0 or negative, passing through 0
                ans2 += (abs(new_pos) // 100) + 1
            elif orig_pos == 0 and new_pos < 0:
                # Starting at 0, going negative - don't count the start
                ans2 += abs(new_pos) // 100
            pos = new_pos
        else:
            new_pos = pos + num
            # Count how many times we pass through 0 going right
            if orig_pos > 0 and new_pos >= 100:
                # We crossed 100 boundary (which is 0 in modulo)
                ans2 += new_pos // 100
            elif orig_pos == 0 and new_pos > 0 and new_pos < 100:
                # Starting at 0, staying in 0-99 range - don't count
                pass
            elif orig_pos == 0 and new_pos >= 100:
                # Starting at 0, going past 100 - don't count the start
                ans2 += (new_pos // 100)
            pos = new_pos
        
        pos %= 100
        
        if pos == 0:
            ans += 1

print(f"Lands on 0: {ans}")
print(f"Passes through 0: {ans2}")
