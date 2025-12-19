# ---------------------------------------------------------------------------------------------------------------------------------------
'''
- Exercícios Listas: Parte 01
'''
# - Questão 78)

valores = list()

maior = 0
menor = 0

for cont in (range(0, 5)):
   valores.append(int(input(f'Posição {cont}º: ')))

   if cont == 0:
      maior = menor = valores[cont]

   else:
      if valores[cont] > maior:
         maior = valores[cont]
      
      if valores[cont] < menor:
         menor = valores[cont]


print('=-' * 40)
print(f'Valores digitados: {valores}')

print(f'Maior valor digitado: {maior} -> Posição: ', end=' ')

for i, v in enumerate(valores):
   if v == maior:
      print(f'{i}º ', end='')

print()

print(f'Menor valor digitado: {menor} -> Posição: ', end=' ')

for i, v in enumerate(valores):
   if v == menor:
      print(f'{i}º ', end='')

print()

