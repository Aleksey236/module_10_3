import threading
import random
from time import sleep
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            adjunction = random.randint(50, 500)

            with self.lock:
                self.balance += adjunction
                print(f"Пополнение: {adjunction}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            cashing_out = random.randint(50, 500)
            print(f"Запрос на {cashing_out}")

            with self.lock:
                if self.balance >= cashing_out:
                    self.balance -= cashing_out
                    print(f"Снятие: {cashing_out}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")
            sleep(0.001)





bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
