#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste.
#Calcular e escrever o valor do novo salário.

salario=float(input("Digite o seu salario atual: "))
reajuste=float(input("Digite o percentual de aumento do seu salario: "))

salarioN= salario*reajuste/100
salarioN= salario+salarioN

print("seu novo salario é: ",salarioN)