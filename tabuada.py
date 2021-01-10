numero = int(input('Digite um número inteiro para ver a sua tabuada: '))
print(
    'Selecione [1] para soma, [2] para subtração, [3] para multiplicação e [4] para divisão.')
opcao = int(input('Qual tabuada você quer ver? '))
for i in range(0, 11):
    if opcao == 1:
        resultado = i + numero
        print(f'{i} + {numero} = {resultado}')
    elif opcao == 2:
        resultado = i - numero
        print(f'{i} - {numero} = {resultado}')
    elif opcao == 3:
        resultado = i * numero
        print(f'{i} x {numero} = {resultado}')
    elif opcao == 4:
        resultado = i / numero
        print(f'{i} / {numero} = {resultado}')
