# calculadora simples
ope = str(input('Qual operação deseja realizar? (soma, subtração, multiplicação ou divisão): '))
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if ope == 'soma':
    print(f'A soma é: {num1 + num2}')

elif ope == 'subtração':
    print(f'A subtração é: {num1 - num2}')

elif ope == 'multiplicação':
    print(f'A multiplicação é: {num1 * num2}')

elif ope == 'divisão':
    print(f'A divisão é: {num1 / num2}')

else:
    print('Você digitou algo errado, tente novamente')
