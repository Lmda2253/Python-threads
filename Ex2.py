
import threading
import time
import random

def calcular_soma(id, valores):
    soma = 0

    for numero in valores:
        soma += numero
        time.sleep(0.2)

    print("Linha", id, "- Valores:", valores)
    print("Soma da linha", id, "=", soma)


threads = []

for id in range(1, 4):
    valores = []

    for i in range(5):
        numero = random.randint(1, 100)
        valores.append(numero)

    t = threading.Thread(
        target=calcular_soma,
        args=(id, valores)
    )

    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Todas as somas foram calculadas!")
