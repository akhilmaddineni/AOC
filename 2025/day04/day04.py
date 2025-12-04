ans = 0 
ans2 = 0
with open("input.txt") as f:
    input = [line.rstrip() for line in f]
    num_rows = len(input)
    num_cols = len(input[0])
    for i in range(num_rows):
        for j in range(num_cols):
            if input[i][j] == '@':
                #check if surrounded by < 4 @ in all 8 directions
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < num_rows and 0 <= nj < num_cols:
                            if input[ni][nj] == '@':
                                count += 1
                if count < 4:
                    ans += 1
    #part2
    while True:
        changed = False
        track_indices = []
        for i in range(num_rows):
            for j in range(num_cols):
                if input[i][j] == '@':
                    #check if surrounded by < 4 @ in all 8 directions
                    count = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = i + di, j + dj
                            if 0 <= ni < num_rows and 0 <= nj < num_cols:
                                if input[ni][nj] == '@':
                                    count += 1
                    if count < 4:
                        ans2 += 1
                        track_indices.append((i, j))
                        changed = True
        for i, j in track_indices:
            input[i] = input[i][:j] + '.' + input[i][j+1:]
        if not changed:
            break
print(ans)
print(ans2)
