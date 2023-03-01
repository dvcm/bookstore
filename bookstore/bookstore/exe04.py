""" Faca um programa que peca 2 numeros inteiros e um numero float 12.4

A produto do dobro do primeiro com metade do segundo.
A soma do triplo do primeri ocom o terceiro.
O terceiro elevado ao cubo.
"""

numero_1 = int(input('digite um numero inteiro: '))
numero_2 = int(input('digite outro numero inteiro: '))
numero_3 = float(input('digite um numero float: '))

resultado_1 = (numero_1 * 2) * (numero_2 / 2)
resultado_2 = numero_1 * 3 + numero_3
resultado_3 = numero_3 ** 3

print(f'Resultado 1: {resultado_1}')
print(f'Resultado 1: {resultado_2}')
print(f'Resultado 1: {resultado_3}')