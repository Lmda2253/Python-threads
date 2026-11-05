
import threading
import time

def executar_thread(id):
    time.sleep(0.5)
    print("Thread #" + str(id))


threads = []

for i in range(1, 6):
    t = threading.Thread(target=executar_thread, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Todas as Threads terminaram!")
