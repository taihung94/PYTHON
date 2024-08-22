# (3 points) You are required to develop a python program that will throw two dice until the top faces of the two dice total to a specified number.
# The output from your program looks something like:
# Enter an integer number of total: 8
# Dice Thrower
# Result of throw: 11+3
# Result of throw: 26+5
# Result of throw: 34+3
# Result of throw: 46+2
# You got your total in 4 throws
import random


def input_num(pomt):
    while True:
        try:
            num = int(input(pomt))
            if num >= 2 and num <= 12:
                return num
            else:
                print("no hop le")
        except ValueError:
            print("invalid")
def main():
    n=input_num("Enter a number: ")
    sum =0
    i=1
    while sum!=n:
        n1=int(random.uniform(1,6))
        n2=int(random.uniform(1,6))
        print(f"Result of throw: {i} {n1}+{n2}" )
        sum=n1+n2
        i+=1
    print(f"You got your total in {i-1} throws")

main()
