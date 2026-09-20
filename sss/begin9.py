a = float(input('введите цену за kg: '))
for i in range(10, 22, 2):
    cost = i*0.1*a
    print(f'{cost}-цена')