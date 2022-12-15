import math

raioLata= float(input("Qual o raio da lata de óleo: "))
alturaLata= float(input("Qual a altura da lata: "))

resultado= round(math.pi*raioLata**2*alturaLata,2)

print(resultado)