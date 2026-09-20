N = int(input('введите число: '))
P = 2*N-1
result = 0 

for i in range(1, P+1, 2):
    result += i
    print(result)