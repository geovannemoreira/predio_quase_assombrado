# "for" contando de 1 a 20 pulando o 13
for andar in range(1, 21):
    if andar !=13:
        print("Andar:", andar)
print()
# Usando loop "for" de trás pra frente
for andar in range(20, 0, -1):
    if andar != 13:
        print("exemplo for:", andar)
print()

# Usando loop while contando de trás para frente e pulando o 13
andar = 20
while andar >= 1:
    if andar != 13:
        print("exemplo while:", andar)
    andar -= 1
print()

