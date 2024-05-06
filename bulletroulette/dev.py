with open("../README.md", "r", encoding="utf-8") as fh:
    readmetxt = fh.read()
with open("../LICENSE", "r", encoding="utf-8") as fh:
    licensetxt = fh.read()

def dev():
    def readme():print(readmetxt)
    def license():print(licensetxt)
    while True:
        exec(input("(roulette)>>> "))