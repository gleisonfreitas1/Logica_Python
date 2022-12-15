n1= float(input("Digite a nota da primeira avaliação"))
n2= float(input("Digite a nota da segunda avaliação"))

notafinal = (n1+n2)/2

if notafinal > 6:
    print("Parabens você foi aprovado")
else:
    print("Infelismente você foi reprovado")