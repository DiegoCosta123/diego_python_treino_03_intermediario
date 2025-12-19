# - Questão 72:

# cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')

# while True:
#    num = int(input('Digite um número entre 0 e 20: '))

#    if 0 <= num <= 20:
#       break

#    print('Tente novamente.', end=' ')

# print(f'Você digitou o número {num} -> "{cont[num]}" ')


# ----------------------------------------------------------------------------------------------------------------------------------------------------
# - Questão 73:

# times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Negra', 'Atlético-GO')

# print('')
# print(f'-> Lista de times do Brasileiro: {times}')

# print(f'\n- Os 5 primeiros times são: {times[0:5]}')
# print(f'- Os 4 últimos times são: {times[-4:]}')
# print(f'- Times em ordem alfabética: {sorted(times)}')
# print(f'\n- O Chapecoense está na {times.index("Chapecoense") + 1}ª posição\n')



# ----------------------------------------------------------------------------------------------------------------------------------------------------
# - Questão 74:

# import random

# numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), )
# print('Os valores sorteados:', end=' ')

# for n in numeros:
#    print(f'{n}', end=' ')

# print(f'\n- Maior valor sorteado: {max(numeros)}')
# print(f'- Menor valor sorteado: {min(numeros)}')



# ----------------------------------------------------------------------------------------------------------------------------------------------------
# - Questão 75:

# print('-' * 50)

# num = (int(input('Digite 1º valor: ')),
#        int(input('Digite 2º valor: ')),
#        int(input('Digite 3º valor: ')),
#        int(input('Digite 4º valor: ')))

# print('-' * 50)
# print(f'Valores digitados: {num}')
# print('-' * 50)

# if 9 in num:
#    print(f'- O valor 9 apareceu {num.count(9)} vezes')
# else:
#    print('- O valor 9 inexiste.')

# if 3 in num:
#    print(f'- O valor 3 apareceu na {num.index(3) + 1}ª posição')
# else:
#    print('- O valor 3 no posição inexiste.')

# print(f'- Valores digitados de par: ', end='')

# for n in num:
#    if n % 2 == 0:
#       print(n, end=' ')

# print('')
# print('-' * 50)



# ----------------------------------------------------------------------------------------------------------------------------------------------------
# - Questão 76:

# listagem = ('Lápis', 1.75,
#             'Borracha', 2,
#             'Caderno', 15.90,
#             'Estojo', 25,
#             'Transferidor', 4.20,
#             'Compasso', 9.99,
#             'Mochila', 120.32,
#             'Canetas', 22.30,
#             'Livro', 34.90,)


# print('-' * 45)
# print(f'{"LISTAGEM DE PREÇO":^40}')
# print('-' * 45)

# for pos in range(0, len(listagem)):
#    if pos % 2 == 0:
#       print(f'{listagem[pos]:.<30}', end='')
   
#    else:
#       print(f'R${listagem[pos]:>7.2f}')
   

# print('-' * 45)



# ----------------------------------------------------------------------------------------------------------------------------------------------------
# - Questão 77:

palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'práticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavra:
   print(f'\nNa palavra "{p.upper()}" temos: ', end='')

   for letra in p:
      if letra.lower() in 'aáeéiíou':
         print(letra, end=' ')

