# tìm số lớn nhất và số nhỏ nhất trong arr

def maxArr(arr):
    # gán max= số âm vô cùng
    max=float("-inf") 
    

    for i in range(len(arr)):
        if max <arr[i]:
            max=arr[i]
        
    return max

def minArr(arr):
    # gán min bằng số dương vô cùng
    min=float("inf")

    for i in range(len(arr)):
        if min >arr[i]:
            min=arr[i]
    return min

def min2(arr):
    min = float("inf")
    for i in range(len(arr)):
        if (arr[i]<min) and (arr[i]!=minArr(arr)):
            min=arr[i]
    return min

def max2(arr):
    # gán max= số âm vô cùng
    max=float("-inf") 
    

    for i in range(len(arr)):
        if max <arr[i] and arr[i]!=maxArr(arr) :
            max=arr[i]        
    return max


###Problem Statement                                            *
#  * Have the function SecondGreatLow(arr) take the array of      *
#  * numbers stored in arr and return the second lowest and second*
#  * greatest numbers, respectively, separated by a space.        *
#  * For example: if arr contains [7, 7, 12, 98, 106] the output  *
#  * should be 12 98. The array will not be empty and will contain*
#  * at least 2 numbers. It can get tricky if there's just        *
#  * two numbers!       


def second_great_low(arr):
    arr = sorted(arr)  # Sắp xếp và loại bỏ các giá trị trùng lặp
    if len(arr) == 1:
        return f"{arr[0]} {arr[0]}"
    return f"{arr[1]} {arr[-2]}"

arr=[98, 7, 12,7, 106]
print(min(arr))
re=f"{arr[1]} {arr[-2]}"
print(second_great_low(arr))
