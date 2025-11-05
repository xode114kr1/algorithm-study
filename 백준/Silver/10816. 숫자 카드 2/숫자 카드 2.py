from collections import defaultdict

n = int(input())
lst_num = list(map(int, input().split()))
dic = defaultdict(int)
for num in lst_num:
    dic[num] += 1

m = int(input())
lst_hav = list(map(int, input().split()))
for card in lst_hav:
    print(dic[card], end=" ")