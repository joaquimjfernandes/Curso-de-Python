print('\033[32;1mDESAFIO 4 -  Dissecando uma Variável\033[m')
print('\033[32;1mALUNO:\033[m \033[36;1mJoaquim Fernandes\033[m')
frase = input('Digite Algo: ')
print('O tipo primitivo desse valor é', type(frase))
print('Só têm Espaços?', frase.isspace())
print('É um Número?', frase.isnumeric())
print('É Alfabético? ', frase.isalpha())
print('É Alfanúmerico? ', frase.isalnum())
print('Está em Maiúscula? ', frase.isupper())
print('Está em Minúsculas? ', frase.islower())
print('Está Capitalizada? ', frase.istitle())
