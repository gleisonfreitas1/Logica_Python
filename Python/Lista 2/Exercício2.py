#Faça um algoritmo que leia a idade de uma pessoa expressa em anos,
#meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
#Considerar ano com 365 dias e mês com 30 dias.

anos= int(input("Digite quantos anos você tem: "))
meses= int(input("digite quantos meses se passaram des de seu ultimo aniversario: "))
dias= int(input("digite a quantidade de dias que se passaram des de seu ultimo mes-versario: "))

diasVividos= anos*365+meses*30+dias

print("a sua quantidade de dias vividos é",diasVividos)