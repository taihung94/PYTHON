def ElementMerger(arr):
    
    while len(arr)>1:
        arr=[abs(arr[i]-arr[i+1])for i in range(len(arr)-1)]

    return arr[0]

print(ElementMerger([5, 7, 16, 1, 2]))
