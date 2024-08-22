# tìm mode của mảng

def findMode(arr):
    temp={}

    for i in arr:
        if i in temp:
            temp[i]+=1

        else: temp[i]=1

    max_val=float('-inf')
    re=None
    for key,value in temp.items():
        if value >max_val:
            max_val=value
            re=key

    return re

arr=[5, 7, 5, 8, 8, 8, 3, 2, 3]
print(findMode(arr))