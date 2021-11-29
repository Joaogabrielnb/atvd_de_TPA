numero = int(input('Digite o numero da pg: '))
PG = int(input('Digite a razão da pg: '))

for n in range (0,6):
    if n == 0:
        print(f'a1 = {numero}')
    else:
        termo = numero*PG
        print(f'a1{n+1} = {numero}')