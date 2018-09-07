#Copyright Ashrith Kanakanala 2018
from itertools import permutations
from sys import exit
import enchant

loop1 = True

def wordfind():
    d = enchant.Dict("en_US")

    seq = str(input("Please Enter Your Seqence: "))
    numb = int(input("Please Enter The Number of Characters in each Iteration: "))

    if len(seq) < numb:
        print("Please Enter a Number greater than the number of characters in your sequence")
        exit()

    comboset = [''.join(w) for w in permutations(seq, numb)]


    for w in set(comboset):

        """print(w)"""
        if d.check(w):
            print(" ")
            print("!!!FOUND!!!")
            print(w)
            print(" ")


while loop1:
    wordfind()
