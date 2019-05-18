import string
from random import choice

def shit_hello_world():
    target = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
    i = 0
    iters = 0
    while True:
        iters += 1
        a = choice(string.ascii_letters + "!" + " ")
        if a == target[i]:
            print(a, end ="")
            i+=1
            if i >= len(target):
                break
        else:
            continue
    print("\nCompleted in {} iterations".format(iters))

if __name__ == "__main__":
    shit_hello_world()
