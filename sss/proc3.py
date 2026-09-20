X = int(input("введите число: "))
Y = int(input("введите число 2: "))
def Mean(X, Y):
    AMean = (X + Y) / 2
    GMean = (X * Y) ** 0.5
    return AMean, GMean
print(Mean(X, Y))