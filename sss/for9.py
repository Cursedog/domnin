A = int(input('введите число A: '))
B = int(input('введите число B: '))
result = 0
for W in (range(A, B+1)):
    result += W**2
print(f'{result}-сумма всех чисел от A до B возведёных в степень 2 ')
