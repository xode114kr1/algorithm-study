n = int(input())
m = int(input())

if n == 1:
    print(8 * m)
elif n == 2:
    if m % 2 == 0 :
        print(1 + 4 * m)
    else:
        print(3 + 4 * m)
elif n == 3:
    print(2 + 4 * m)
elif n == 4:
    if m % 2 == 0 :
        print(3 + 4 * m)
    else:
        print(1 + 4 * m)
elif n == 5:
    print(4 + 8 * m)