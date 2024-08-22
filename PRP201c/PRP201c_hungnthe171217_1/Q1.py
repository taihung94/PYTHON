
import random
def input_count(pomt):
    while True:
        try:
            n=int(input(pomt))
            if n>0:
                return n
            else:
                print("The number must be greater than 0. Please try again.")
        except ValueError:
            print("Invalid value.Please try again.")
def input_num ( pomt1, pomt2 ) :
    while True:
        try:
            start=int(input(pomt1))
            end=int(input(pomt2))
            if start < end:
                return start,end
            else:
                print("Invalid range. The Start must be less than the End of the Range.")
        except ValueError:
            print("Invalid value.Please try again.")
def check_unique(list1):
    for i in range(len(list1)-1):
        for j in range(i+1,len(list1)):
            if list1[i] == list1[j]:
                return False
    return True
def unique_int(start,end,n):
    if n>= ((end-1)-(start+1)+1):
        raise Exception()
    # return [int(random.uniform(start, end)) for i in range(n)]
    li=[int(random.uniform(start, end)) for i in range(n)]
    if check_unique(li):
        return li

def main():
    while True:
        try:
            start,end= input_num("Enter the start of the range: ","Enter the end of the range: ")
            count_int=input_count("How many unique integers would you like to generate? ")
            gener_list=unique_int(start,end,count_int)
            print("Generated list of unique integers: ",gener_list)
            avg=sum(gener_list)/len(gener_list)
            print(f"Average of the integers: {avg:.1f}")
            print("Min value in the list: ", min(gener_list))
            break
        except Exception:
            print("The range not enough value to be unique. Please input again.")
if __name__ == '__main__':
    main()