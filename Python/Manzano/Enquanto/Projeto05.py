contadora = 0
expoente = 2
resultado = 3

print("3 elevado a 0 é 0")
print("3 elevado a 1 é 3")

while (contadora <= 15):
    while (expoente <= contadora):
        resultado = resultado * 3
        print("3 elevado a",contadora,"é",resultado)
        expoente = expoente + 1;
    contadora = contadora + 1;
