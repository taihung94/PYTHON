# bài tập cho mảng sao là chuỗi tăng cho tổng các phần tử đầu phải nhỏ hơn phần tử cuối

def kt_arr(arr):
    for i in range(len(arr)-1):
        if int(arr[i])> int(arr[i+1]):
            return False
        
    if len(arr)==1: return True

    if sum(arr[i] for i in range(0,len(arr)-1)) < arr[-1]:
        return True
    return False

arr=[1,3,2,8]

print(kt_arr(arr))

