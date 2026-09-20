A = int(input('введите число A'))
B = int(input('введите число B'))
count = 0
for i in range(A-1, B, -1):
    count += 1
    print(i)

print(f'колличество:{count}')
