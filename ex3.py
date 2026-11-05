
import threading
import time
import random

DISTANCIA_MAXIMA = 30
TAMANHO_MAXIMO_SALTO = 5

def corrida(id):
    distancia = 0

    while distancia < DISTANCIA_MAXIMA:
        salto = random.randint(1, TAMANHO_MAXIMO_SALTO)

        distancia += salto

        if distancia > DISTANCIA_MAXIMA:
            distancia = DISTANCIA_MAXIMA

        print(
            "Sapo", id,
            "saltou", salto, "cm.",
            "Distancia percorrida:", distancia, "cm"
        )

        time.sleep(0.3)

    print("Sapo", id, "CHEGOU!")

 
threads = []

for i in range(1, 6):
    t = threading.Thread(target=corrida, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("FIM DA CORRIDA!")
