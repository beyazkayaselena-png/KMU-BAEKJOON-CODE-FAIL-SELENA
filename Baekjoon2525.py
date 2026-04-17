h, m = map(int, input().split())

cooking_time = int(input())

m += cooking_time

h += m // 60
m %= 60

h %= 24

print(h, m)
