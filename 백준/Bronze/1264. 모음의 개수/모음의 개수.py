while 1:
    str = input()
    if str == "#":
        break
    cnt = 0
    for c in str:
        if c.lower() in ["a", "e", "i", "o", "u"]:cnt += 1
    print(cnt)