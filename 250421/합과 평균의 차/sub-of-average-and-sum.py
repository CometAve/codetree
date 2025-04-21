a, b, c = map(int, input().split())
total = a + b + c
avg = int(total / 3)
diff = total - avg
print(f'{total}\n{avg}\n{diff}')