
ans = 0
ans2 = 0

def generate_valid_numbers(L: int, U: int):
    """
    Return a list of numbers in [L, U] that are formed by repeating a digit sequence twice.
    Optimized: Instead of checking every number, generate valid numbers directly.
    """
    valid_numbers = []

    # Determine digit lengths in range
    min_len = len(str(L))
    max_len = len(str(U))

    # Only even digit lengths matter
    for d in range(min_len, max_len + 1):
        if d % 2 != 0:
            continue  # skip odd lengths
        k = d // 2

        # Generate all sequences of length k
        start = 10 ** (k - 1)  # first digit cannot be zero
        end = 10 ** k

        for seq in range(start, end):
            num = int(str(seq) * 2)
            if L <= num <= U:
                valid_numbers.append(num)

    return valid_numbers


def generate_repeated_at_least_twice(L: int, U: int):
    """
    Generate all numbers in [L, U] that are formed by repeating a block at least twice.
    Much faster than checking every number when the range is large.
    """
    out = set()
    min_len = len(str(L))
    max_len = len(str(U))

    for d in range(min_len, max_len + 1):
        # Boundaries for this digit length
        lo = max(L, 10**(d - 1))
        hi = min(U, 10**d - 1)
        if lo > hi:
            continue

        # Try block lengths k that divide d, with r = d // k >= 2
        for k in range(1, d // 2 + 1):
            if d % k != 0:
                continue
            r = d // k
            if r < 2:
                continue

            start = 10**(k - 1)      # block cannot start with 0
            end = 10**k
            for block in range(start, end):
                num = int(str(block) * r)
                if lo <= num <= hi:
                    out.add(num)

    return sorted(out)



with open("input.txt", 'r') as f:
    line = f.readline().rstrip()
    ranges = line.split(',')
    int_ranges = []
    for r in ranges:
        a, b = r.split('-')
        int_ranges.append((a, b))
    print(int_ranges)
    #even numbers of digits 
    for a,b in int_ranges : 
        ans += sum(generate_valid_numbers(int(a), int(b)))
        ans2 += sum(generate_repeated_at_least_twice(int(a), int(b)))
print(ans)
print(ans2)
