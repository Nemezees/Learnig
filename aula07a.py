# nome = input('Qual teu nome?')
# print('Seja bem vindo{:=^20}'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s} \nA subtração é {su} \nA multiplicação é {m} \na divisão é {d:.5} '
      f'z\nA divisão inteira é {di} \nE a exponenciação é {e}')
