# Write a program that ask the user how many integers they want to generate. It should then generate that many integers randomly which is range from 1 to 100 and then store them in a list.
# After the list is populated, the program will calculate and display the average of these numbers, and also display the smallest and highest value in the list.
# Result of the program:
# How many random integers would you like to generate? -5
# Please enter a positive integer.
# How many random integers would you like to generate? a
# Invalid input. Please enter a positive integer.
# How many random integers would you like to generate? 5
# Generated list of integers: [60, 3, 66, 49, 62]
# Average of the numbers: 48.00
# Smallest number: 3
# # Largest number: 66
import random


def input_ran(pomt):
    while True:
        try:
            n=int(input(pomt))
            if n>0:
                return n
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
def main():
    n=input_ran("How many random integers would you like to generate?")
    random_list=[int(  random.uniform(0,100) )for i in range(n)]
    print(f"Generated list of integers:{random_list}")
    avg=sum(random_list)/len(random_list)
    print(f"Average generated list is {avg: .2f}")
    print("min= ",min(random_list))

if __name__=="__main__":
    main()