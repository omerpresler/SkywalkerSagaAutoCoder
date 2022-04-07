from time import sleep

import pydirectinput

firstRow = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
secondRow = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
thirdRow = ['buffer1', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
fourthRow = ['buffer2', 'buffer3', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
rows = [firstRow, secondRow, thirdRow, fourthRow]
kbMap = {}

x, y = 0, 3
for row in rows:
    for c in row:
        kbMap[c] = [x, y]
        x += 1
    y -= 1
    x = 0


def moveToLetter(loc):
    currX, currY = kbMap['1']
    locX, locY = loc

    for _ in range(locX - currX):
        pydirectinput.press("d")

    for _ in range(currY - locY):
        pydirectinput.press("s")


def moveToOne(loc):
    for _ in range(loc[1] + 1):
        pydirectinput.press("s")


def typeWord(word):
    word = word.lower()
    for ch in word:
        moveToLetter(kbMap[ch])
        pydirectinput.press(" ")
        moveToOne(kbMap[ch])

    sleep(1.5)
    pydirectinput.press("e")


if __name__ == "__main__":
    sleep(8)
    f = open("codes.txt", "r")
    f = f.read()
    for word in f.split('\n'):
        word = word.split(' ')[0]
        typeWord(word)
