# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!
soma = lambda num1, num2: num1 + num2

subtracao = lambda num1, num2: num1 - num2

multiplcacao = lambda num1, num2: num1 * num2

divisao = lambda num1, num2: num1 // num2
print("\n******************* Python Calculator *******************")
loop = True
while loop:
	print('1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão')
	op = int(input('Digite sua opção[1\2\3\4]'))
	if op == 1:
		print('Soma')
		num1 = int(input('Digite o primeiro valor: '))
		num2 = int(input('Digite o segundo valor: '))
		print(f'A soma de {num1} + {num2} é = ', soma(num1, num2))
	elif op == 2:
		print('Subtração')
		num1 = int(input('Digite o primeiro valor: '))
		num2 = int(input('Digite o segundo valor: '))
		print(f'A subtração de {num1} - {num2} é = ', subtracao(num1, num2))
	elif op == 3:
		print('Multiplicação')
		num1 = int(input('Digite o primeiro valor: '))
		num2 = int(input('Digite o segundo valor: '))
		print(f'A multiplicação de {num1} x {num2} é = ', multiplcacao(num1, num2))
	elif op == 4:
		print('Divisão')
		num1 = int(input('Digite o primeiro valor: '))
		num2 = int(input('Digite o segundo valor: '))
		print(f'A divisão inteira de {num1} / {num2} é = ', divisao(num1, num2))
	else:
		print('Opção inválida!')

	d = input('Quer continuar?')[0].upper()
	
	if d == 'N':
		loop = False

print('Encerrando o programa')