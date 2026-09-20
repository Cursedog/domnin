N = int(input('введите число: '))
result = 1
for i in range(1, N+1):
    result *= i*0.1+1
print(result)