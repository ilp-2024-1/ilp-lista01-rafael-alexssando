# 1. Calculadora Simples: Solicite ao usuário para inserir dois valores numéricos,
# realize as operações de soma, subtração, multiplicação e divisão, e ao final exiba
# os valores de cada uma das operações.

# n1 = int(input('Digite um número inteiro:'))
# n2 = int(input('Digite um número inteiro:'))
# soma = n1 + n2
# subtracao = n1 - n2
# multiplicacao = n1 * n2
# divisao = n1 / n2
# print('A soma dos valores {} e {} é igual a {}'.format(n1, n2, soma))
# print('A subracao dos valores {} e {} é igual a {}'.format(n1, n2, subtracao))
# print('A multiplicação dos valores {} e {} é igual a {}'.format(n1, n2, multiplicacao))
# print('A divisão dos valores {} e {} é igual a {}'.format(n1, n2, divisao))



# 2. Conversor de Temperatura: Solicite ao usuário um valor de temperatura em graus
# Celsius, converta-a para Fahrenheit e exiba o resultado da conversão.

# temperatura = float(input('Insira um valor de temperatura em graus celsius: '))
# conversao = temperatura * 1.8 + 32
# print('A conversão de {} graus celsius em fahrenheit é {} '.format(temperatura, conversao))



# 3. Área do Círculo: Solicite ao usuário um valor do raio de um círculo, calcule sua
# área e exiba o resultado do cálculo.

# raio = float(input('Insira o valor do raio de um círculo: '))
# area = 3.14 * (raio * raio) 
# print('A áreo do cículo é {}'.format(area))



# 4. Área do Triângulo: Solicite ao usuário um valor da base e da altura de um
# triângulo, calcule sua área e exiba o resultado do cálculo.

# base = float(input('Insira a base do triângulo: '))
# altura = float(input('Insira a altura do triângulo: '))
# area =  base * altura / 2
# print('A área do triângulo é {}'.format(area))




# 5. Volume da Esfera: Solicite ao usuário um valor do raio de uma esfera, calcule seu
# volume e exiba o resultado do cálculo.

# raio = float(input('Insira o raio de uma esfera: '))
# volume = 4/3 * 3.14 * raio*raio*raio
# print('O volume da esfera é {:.2f}'.format(volume))



# 6. Calculadora de Média Aritmética: Solicite ao usuário para que ele insira três
# valores de notas, realize o cálculo da média aritmética e em seguida exiba os três
# valores digitados pelo usuário e o resultado do cálculo.



# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))
# media = (n1 + n2 + n3) / 3
# print('A média das notas {} , {} e {} é de {}'.format(n1, n2, n3, media))



# 7. Calculadora de Média Ponderada: Solicite ao usuário para que ele insira os
# valores de 4 notas e seus respectivos pesos, em seguida realize o cálculo da média
# pondera e exiba o resultado do cálculo.

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Diigite a segunda nota: '))
# n3 = float(input('Dogite a terceira nota: '))
# n4 = float(input('Digite a quarta nota: '))
# p1 = int(input('Digite o peso da primeira nota: '))
# p2 = int(input('Digite o peso da segunda nota: '))
# p3 = int(input('Digite o peso da terceira nota: '))
# p4 = int(input('Digite o peso da quarta nota: '))
# media_ponderada = (n1 * p1 + n2 * p2 + n3 * p3 + n4 * p4) / (p1 + p2 + p3 +p4)
# print(media_ponderada)



# 8. Equação de Segundo Grau: Solicite ao usuário os valores de “a”, “b”, “c” e “x”, em
# seguida resolva uma equação quadrática do tipo y = ax2 + bx + c e exiba o valor
# de y para o usuário.

# a = float(input('Insira o valor de "a": '))
# b = float(input('Insira o valor de "b": '))
# c = float(input('Insira o valor de "c": '))
# x = float(input('Insira o valor de "x": '))
# y = a * x**2 + b * x + c
# print('O valor do "y" dessa equação quadrárica é {}'.format(y))



# 9. Calculadora de IMC: Solicite ao usuário os valores de peso (kg) e altura (m),
# calcule o índice de massa corporal (IMC), sabendo que ��� = !"#$
# %&'()%!, em seguida
# exiba o valor do IMC calculado.

# peso = float(input('Qual seu peso: '))
# altura = float(input('Qual a sua altura: '))
# imc = peso/ (altura * altura)
# print('O seu índice de massa corporal é de {:.2f}'.format(imc))



# 10.Tabuada: Solicite ao usuário um valor numérico, em seguida, exiba a tabuada de
# um número específico (por exemplo, 5). O programa deverá ter como saída:
# 5x1 = 5; 5x2 = 10; 5x3 = 15; 5x4 = 20; 5x5 = 25; 5x6 = 30; 5x7 = 35; 5x8 = 40; 5x9
# = 45; 5x10 = 50;

# num = int(input('Digite um número para ver sua tabuada:'))
# print('{} x {} = {}'.format(num, 1, num * 1))
# print('{} x {} = {}'.format(num, 2, num * 2))
# print('{} x {} = {}'.format(num, 3, num * 3))
# print('{} x {} = {}'.format(num, 4 , num * 4))
# print('{} x {} = {}'.format(num, 5 , num * 5))
# print('{} x {} = {}'.format(num, 6, num * 6))
# print('{} x {} = {}'.format(num, 7, num * 7))
# print('{} x {} = {}'.format(num, 8, num * 8))
# print('{} x {} = {}'.format(num, 9, num * 9))
# print('{} x {} = {}'.format(num, 10, num * 10))


# 11.Conversão de Segundos para o Formato HORA:MINUTO:SEGUNDO: Solicite
# ao usuário um valor numérico correspondente à quantidade de segundos, em
# seguida converta o valor para o formato de HORA:MINUTO:SEGUNDO.


segundos = int(input("Digite a quantidade de segundos: "))
horas = segundos // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60
segundos_finais = segundos_restantes % 60

print(f"O valor convertido é {horas:02d}:{minutos:02d}:{segundos_finais:02d}")