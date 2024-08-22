# tìm kiếm tuần tự Linear search

def linear_search( s,arr):
    
    for i in range(len(arr)):
        if s==arr[i]:
            return i
    return -1

# bubble sort

# def swap(a,b):
#     temp=a
#     a=b
#     b=temp

# def buble_sort(arr):
#     for i in range(0,len(arr)-1):
#         for j in range (0,len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#     return arr

# arr=[1,2,4,8,3,1]
# arr1=buble_sort(arr)
# print(buble_sort(arr))



# fibonacci
# def fibo(n):
#     if n <=2: return 1
#     return fibo(n-1)+fibo(n-2)

# for i in range(6):
#     print(fibo(i),end=" ")

arr=[1,2,3,5,6]
arr=arr[:-1]
print(arr)
