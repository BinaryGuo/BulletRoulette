from time import sleep as asleep
from multiprocessing import Process,Queue
from traceback import print_exc as pe

def timering(out):
    while True:
        asleep(10)
        out.put(1)

class shark:
    def __init__(self):
        self.heavy = 0
        self.mood = 0
        self.sleeping = 0

    def eat(self):
        self.heavy += 1
        print("eating...")
        asleep(1)
        print("huu...")

    def play(self):
        self.mood += 1
        print("playing...")
        asleep(1)
        print("good!")

    def sleep(self):
        self.sleeping += 1
        print("sleeping...")
        asleep(1)
        print("wake")
    
    def kill(self):
        print("\nshark dead!")
        print(f"heavy:{shk.heavy}")
        print(f"mood:{shk.mood}")
        print(f"sleep:{shk.sleeping}")
        timer.terminate()
        exit()

shk = shark()
ca = 0
q1 = Queue()
q2 = Queue()
timer = Process(target = timering,args = (q2,))
timer.start()
while True:
    while True:
        try:
            exec("shk." + input("operation: ") + "()")
            break
        except:
            print("operation error!")
    if q2.empty() == False:
        q2.get()
        shk.heavy -= 1
        shk.mood -= 1
        shk.sleeping -= 1
        if q2.empty() == False:
            q2.get()
            shk.heavy -= 1
            shk.mood -= 1
            shk.sleeping -= 1
    print(f"heavy:{shk.heavy}")
    print(f"mood:{shk.mood}")
    print(f"sleep:{shk.sleeping}")
    if shk.heavy == 3 or shk.heavy == -3 or shk.mood == 3 or shk.mood == -3 or shk.sleeping == 3 or shk.sleeping == -3: shk.kill()