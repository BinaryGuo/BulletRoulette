from os.path import dirname

with open(f"{dirname(__file__)}/intros/README.md", "r", encoding="utf-8") as fh:
    readmetxt = fh.read()
with open(f"{dirname(__file__)}/intros/LICENSE", "r", encoding="utf-8") as fh:
    licensetxt = fh.read()

def readme():print(readmetxt)
def license():print(licensetxt)

def run():
    while True:
        exec(input("(roulette)>>> ") + "()")