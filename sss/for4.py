p = int(input('введите цену конфет: '))
k = int(input('введите кг конфет: '))
for i in range(1, k+1):
    print(f'{i} кг конфет будет стоить {i * k} рублей')