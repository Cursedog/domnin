A = int(input('введите число A'))
B = int(input('введите число B при B > A'))
count = 0
for i in range(A, B+1):
    count += 1
    print(i)

print(f'колличество:{count}')
