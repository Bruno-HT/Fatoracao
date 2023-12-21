
def criar_lista_numeros_primos():
    numeros = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i in range (24, 1000):
        divisores = []
        for ii in range (2, i+1):
            resto = i%ii
            if resto == 0:
                divisores.append(ii)
        if len(divisores) == 1:
            numeros.append(i)
    return numeros

def calculo_fatoracao(fatorar, controle):
    fatorado = []
    while fatorar != 1:
        for index in range (0, len(numeros_primos)):
            resto = fatorar % numeros_primos[index]
            if resto == 0:
                fatorado.append(numeros_primos[index])
                fatorar = fatorar / numeros_primos[index]
    return fatorado

print('\n\n\n')
print('**************************************************')
print('*** VAMOS ESTUDAR FATURAÇÃO POR NÚMEROS PRIMOS ***')
print('**************************************************\n')
numeros_primos = criar_lista_numeros_primos()
fatorar = int(input('Digite um número positivo para fatorarmos: '))
if (fatorar <= 0):
    print('Por favor, tente novamente digitando um número maior que 0!')
controle = fatorar
resultado = calculo_fatoracao(fatorar, controle)
resultado.sort()

print('\n')
print(f'Você pediu para fatorar o número: {controle}')
print(f'E o resultado foi: {resultado}')
print('\n\n\n')