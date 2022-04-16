print('----------- TABLA DE MULTIPLICAR ------------')
print('''      0   1   2   3   4   5   6   7   8   9
---------------------------------------------''', end='')
for i in range(10):
    print()
    contador = 0
    for j in range(10):
        producto = 0
        cantidad = 0
        if contador == 0:
            print(i,':', end='')
        while cantidad <j:
            producto += i
            cantidad += 1
        print(f'{producto:4d}', end='')
        contador +=1 
print() 