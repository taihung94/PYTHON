#  cho mảng gồm nhiều từ, in ra từ có số chữ cái lớn thứ 3, nếu có 3 từ có số từ lớn bằng nhau thì lấy thằng cuối cùng
# *                                                              *
#  * Problem Statement                                            *
#  * Have the function ThirdGreatest(strArr) take the array of    *
#  * strings stored in strArr and return the third largest word   *
#  * within it. So For Example:                                   *
#  * if strArr is ["hello", "world", "before", "all"] your output *
#  * should be world because "before" is 6 letters long,          *
#  * and "hello" and "world" are both 5, but the output should be *
#  * world because it appeared as the last 5 letter word in the   *
#  * array. If strArr was ["hello", "world", "after", "all"] the  *
#  * output should be after because the first three words are all *
#  * 5 letters long, so return the last one. The array will have  *
#  * at least three strings and each string will only contain     *
#  * letters.                                                     *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: new string[] {"coder","byte","code"}                *
#  * Output 1: code                                               *
#  *                                                              *
#  * Input 2: new string[] {"abc","defg","z","hijk"}              *
#  * Output 2: abc                  
def find3(arr):
    # tìm từ có độ dài lớn thứ 3
    arr_temp=[]
    for i in range(len(arr)):
        arr_temp.append(len(arr[i]))
    arr_temp=sorted(arr_temp,reverse=True) # sắp xếp giảm dần 
    count=arr_temp[2]
    # tìm từ đó
    re=""
    for word in arr:
        if len(str(word))==count:
            re=word
    return re

arr=["abc","defg","z","hijk"]
print(find3(arr))
