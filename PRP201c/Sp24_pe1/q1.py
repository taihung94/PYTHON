# After the list is populated, the program calculates and displays the average of these numbers and also displays the minimum value in the list.
# Result of the program:
# How many random floating-point numbers would you like to generate? -5
# Please enter a number greater than 0.
# How many random floating-point numbers would you like to generate? a
# Invalid input. Please enter an integer.
# How many random floating-point numbers would you like to generate? 5
# Enter the lower bound of the range: 0.5
# Enter the upper bound of the range: -0.5
# Invalid range. The lower bound must be less than the upper bound.
# Enter the lower bound of the range: 0.5
# Enter the upper bound of the range: 1.5
# Generated list of floating-point numbers:[0.57, 0.90, 1.25, 0.92, 1.40]
# Average of the numbers: 1.01
import random
def get_number(st):
    while True:
        try:
            n=input(st)
            if int(n)>0:
                return n
            else:
                print("Please enter a number greater than 0")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_range(st1,st2):
    while True:
        try:
            n1=float(input(st1))
            n2=float(input(st2))
            if n1<n2:
                return n1,n2
            else: 
                print("Invalid range. The lower bound must be less than the upper bound.")
        except ValueError:
            print("Invalid range. The lower bound must be less than the upper bound.")

def get_list_random(n1,n2,n):
    return [round(random.uniform(n1,n2),2) for i in range(int(n))]

def main():
    n=get_number("How many random floating-point numbers would you like to generate?")
    n1,n2=get_range("Enter the lower bound of the range:","Enter the upper bound of the range:")
    li=[]
    li=get_list_random(n1,n2,n)

    print(f"Generated list of floating-point numbers: {li}")
    ave=sum(li)/len(li)
    print(ave)
if __name__=="__main__":
    main()