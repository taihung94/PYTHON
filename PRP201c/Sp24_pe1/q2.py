# Hint: A perfect number is a positive integer that is equal to
# the sum of its proper divisors,excluding itself. F
# For example, 6 is a perfect number because its divisors are 1, 2, and 3,and 1+2+3=6.
# The content of data 1.txt file:12,3,5,28,-1,6,496,23,8128,34,55,8,20,22,2,10,11,8128,7,28
# Result of the program:
# Perfect numbers from the file: [28, 6, 496, 8128, 8128, 28]
# Occurrences of each perfect number: {496: 1, 28:2, 6: 1, 8128: 2}
# Number(s) with the highest frequency: 28, 8128

def perfect_num(n):
    sum=0
    for i in range(1,n):
        if n%i==0 :
            sum+=i
    if sum==n:
        return True
    return False

def main():
    with open("data_1.txt","r") as file:
        li_num = file.read().strip().split(",")
    num=[int(i) for i in li_num if i.isdigit()]
    num_per=[i for i in num if perfect_num(i)]

    dic={}

    for i in num_per:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    
    print(dic)
    max_c=max(dic.values())

    re = [key for key, value in dic.items() if value == max_c]

    print("ffsfs" , ", ".join(map(str,re)))

main()
