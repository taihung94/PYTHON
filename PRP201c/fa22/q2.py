
def file_re(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().strip("[]")
            li=text.split(",")
            numbers = [int(i.strip(" '"))for i in li]
            combi=[]
            for i in range(len(numbers)-1):
                for j in range(i+1,len(numbers)):
                    st=""
                    st=str(numbers[i])+str(numbers[j])
                    combi.append(int(st))
        print(f"lít ban đau: {text}")
        print(li)
        print(f"list sau: {combi}")
    except FileNotFoundError:
        print('File not found')

file_re('Text.txt')