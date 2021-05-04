#Calculadora Simples

numero1 = 0
numero2 = 0
resultado = 0
operacao = ''
while True:
    numero1 = int(input('Digite o primeiro numero: '))
    operacao = input('Digite a operação: ')
    numero2 = int(input('Digite o segundo numero: '))

    if operacao == '+':
        resultado = numero1 + numero2
        print(str(numero1) + ' ' +  str(operacao) + ' ' + str(numero2) + ' = '  + str(resultado))
    elif operacao == '-':
        resultado = numero1 - numero2
        print(str(numero1) + ' ' +  str(operacao) + ' ' + str(numero2) + ' = '  + str(resultado))
    elif operacao == '/':
        resultado = numero1 / numero2
        print(str(numero1) + ' ' +  str(operacao) + ' ' + str(numero2) + ' = '  + str(resultado))
    elif operacao == '*':
        resultado = numero1 * numero2
        print(str(numero1) + ' ' +  str(operacao) + ' ' + str(numero2) + ' = '  + str(resultado))
    else:
        resultado = 'Operação inválida!'
        print(resultado)
#Primeiro projeto terminado!