A = int(input('введите число A: '))
B = int(input('введите число B: '))
result = 1
for i in range(A, B+1):
    result *= i
print(f'{result}-произведение чисел от A до B')
