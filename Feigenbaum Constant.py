lanbda = 5
listaPrincipal = list()
listaPeriodos = list()

while lanbda > 4 or lanbda < 0:
    lanbda = float(input('Digite um número real (entre 0 a 4 inclusive) que corresponderá ao lambda: '))
    if lanbda > 4 or lanbda < 0:
        print("Valor fora do intevalo (0 a 4). Tente novamente.")
Xn = 2
while Xn < 0 or Xn > 1:
    Xn = float(input('Digite um número real (entre 0 a 1 inclusive) que corresponderá ao Xn: '))
    if Xn < 0 or Xn > 1:
        print("Valor fora do intevalo (0 a 1). Tente novamente.")

contador = Xn
periodo = 0
Xanterior = Xn
print(f"Xn = {Xn}")

for count in range(1, 10000):
    if listaPrincipal.count(Xanterior) > 1: # <<< para quando identifica o ciclo
        break
    print(f"Xn+{count} = {lanbda * Xanterior * (1 - Xanterior)}")
    Xanterior = lanbda * Xanterior * (1 - Xanterior)

    listaPrincipal.append(Xanterior)
    if listaPrincipal.count(Xanterior) > 1:
        if (Xanterior in listaPeriodos) == False:
            listaPeriodos.append(Xanterior)

print(f"lambda: {lanbda}")
print(f"Xn: {Xn}")
print(f'Período : {len(listaPeriodos)}')
print(f"Termos: {listaPeriodos}")
