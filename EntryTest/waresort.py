def WaveSorting(arr):
    arr.sort()
    array1 = arr[:len(arr)//2]
    array2 = arr[len(arr)//2:]
    for i in range(len(array1)):
        if array1[i] >= array2[i]:
            return False
    return True

# Đoạn code dưới đây là để thực thi hàm WaveSorting với đầu vào từ người dùng (tương tự readline() trong JavaScript)
# arr = list(map(int, input().strip().split()))
arr2=[0, 4, 22, 4, 14, 4, 2] 
print(WaveSorting(arr2))
