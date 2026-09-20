N = int(input('введите число: '))
result=0
P = N*2
for i in range(N, P+1):
    result += i**2
print(result)