#tìm và in ra số fibo naci

def input_num(pomt):
    while True:
        try:
            n=int(input(pomt))
            if n>=0:
                return n
            else:
                print("input agan")
        except ValueError:
            print("invalid")

def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)
def main():
    n=input_num("input number")
    for i in range(n+1):
        print(fibo(i), sep=" ",end=" ")

if __name__ == '__main__':
    main()