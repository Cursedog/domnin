N = int(input('введите число: '))
result = 0
for i in range(1, N+1):
    result += 1/i
print(f'{result}-сумма едениц делённых на числа от 1 до N')
