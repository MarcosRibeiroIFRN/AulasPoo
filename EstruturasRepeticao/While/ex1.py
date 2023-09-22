""""1. O cálculo do fatorial de um número é dado pela multiplicação desse
número com todos os antecessores inteiros positivos. Por exemplo, o
fatorial de 5 é 5! = 5*4*3*2*1 = 120. Escreva um programa que
solicite um número e apresente o resultado do seu fatorial."""
num1=int(input("Digite o número: "))
ctt1=num1
resul1=1
while(ctt1>1):
    resul1= resul1 *(ctt1)
    ctt1=ctt1-1
print(resul1)    
