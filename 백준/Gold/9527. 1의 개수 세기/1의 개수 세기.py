def count_ones(x):
    total = 0
    bit = 1

    while (2 ** (bit - 1)) <= x:
        size = 2 ** bit
        cycle_cnt = (x + 1) // size
        module_cnt = (x + 1) % size

        total += cycle_cnt * size // 2
        if module_cnt > size // 2:
            total += module_cnt - size // 2
        bit += 1
    return total


a, b = map(int, input().split())
print(count_ones(b) - count_ones(a - 1))