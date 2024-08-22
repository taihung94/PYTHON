# bài tập kiểm tra trong một câu sao cho từ nào có số lượng ký tự lặp lại nhiều nhất thì in ra output


# def LetterCountI(strParam):
# 	str_arr = strParam.split()
# 	count = 0
# 	greatest_length = '-1'
	
# 	for i in range(len(str_arr)):
# 		for j in range(len(str_arr[i])):
# 			new_count = 0
# 			for k in range(j+1, len(str_arr[i])):
# 				if str_arr[i][j] == str_arr[i][k]:
# 					new_count+=1
# 			if new_count > count:
# 				count = new_count
# 				greatest_length = str_arr[i]
# 	return greatest_length
	
# print(LetterCountI(input()))

def count_repeated_characters(s):
    # Tạo từ điển để đếm số lần xuất hiện của từng ký tự
    dic={}
    
    # Đếm số lần xuất hiện của từng ký tự
    for char in s:
        if char in dic:
            dic[char]+=1
        else : 
            dic[char]=1    
    # Đếm số lượng ký tự xuất hiện hơn 1 lần
    count_char=0
    for i in dic.values():
        if i>1: count_char+=1        
    return count_char
    
    
    
str=input()
st=str.split()
count_max=-1
result=""
for i in st:
    if count_repeated_characters(i)>count_max : 
         count_max=count_repeated_characters(i)
         result=i
         
if count_max!= -1:
    print(result)
else: 
    print(-1)
    
