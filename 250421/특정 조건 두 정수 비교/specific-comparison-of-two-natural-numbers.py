a, b = map(int, input().split())
f = -1
s = -1
if a < b:
    f = 1
else:
    f = 0

if a == b:
    s = 1
else:
    s = 0

print(f, s)