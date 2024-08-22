def ScaleBalancing(strArr):
    
    # Parse the input strings
    weights = eval(strArr[0])
    available_weights = eval(strArr[1])
    
    left_weight = weights[0]
    right_weight = weights[1]
    difference = abs(left_weight - right_weight)
    
    # trường hợp chỉ cần 1 quả
    for weight in available_weights:
        if weight == difference:
            return str(weight)
    
    # Trường hợp cần 2 quả nhưng chỉ cho 1 bên cân=> hiệu 2 bên trái phải = tổng 2 quả cân thêm vào
    for i in range(len(available_weights)-1):
        for j in range(i+1,len(available_weights)):
            if difference == (available_weights[i]+available_weights[j]):
                return f"{available_weights[i]} {available_weights[j]}"
            
    # Trường hợp cần 2 quả nhưng cho mỗi bên cân 1 quả => hiệu trái phải = hiệu 2 quả cân
    for i in range(len(available_weights)-1):
        for j in range(i+1,len(available_weights)):
            if difference == abs(available_weights[i]-available_weights[j]):
                return f"{available_weights[i]} {available_weights[j]}"    
    
    # Trường hợp mà 2 quả cân bằng nhau=> chứa 2 quả cân nhau
    if left_weight[0]==left_weight[1]:
        for i in range(len(available_weights)-1):
            if int(available_weights[i])==int(available_weights[i+1]):
                return f"{available_weights[i]} {available_weights[i]}" 
    # If no combination works, return "not possible"
    return "not possible"

# Example usage
input1 = ["[3, 3]", "[1, 2, 7, 7]"]
input2 = ["[13, 4]", "[1, 2, 3, 5, 14]"]

print(ScaleBalancing(input1))  # Output: 1
print(ScaleBalancing(input2))  # Output: 3,6
