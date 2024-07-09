print('TRANFORMADOR DE METROS EM CENTIMETROS E MILIMETROS')

comprimento = float(input('Digite a metragem que deseja tranformar: '))
print(f'A metragem em KILOMETROS É: {comprimento / 1000} KM \n'
      f'Em HECTOMETRO é: {comprimento / 100}HM \n'
      f'Em DECAMENTRO é: {comprimento / 10}DAM \n'
      f'Em METRO é: {comprimento}M \n'
      f'Em DECIMETRO é: {comprimento * 10}DM\n'
      f'Em CENTIMETRO é: {comprimento * 100}CM \n'
      f'E em MILIMETRO é: {comprimento * 1000}MM')
