# /****************************************************************
#  *             CODERBYTE SWIPE CASE TWO CHALLENGE               *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function SwapII(str) take the str parameter and swap*
#  * the case of each character. Then, if a letter is between two *
#  * numbers (without separation), switch the places of the two   *
#  * numbers.                                                     *
#  * For example: if str is "6Hello4 -8World, 7 yes3"             *
#  * the output should be 4hELLO6 -8wORLD, 7 YES3.                *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "Hello -5LOL6"                                      *
#  * Output 1: hELLO -6lol5                                       *
#  *                                                              *
#  * Input 2: "2S 6 du5d4e"                                       *
#  * Output 2: 2s 6 DU4D5E                                        *
#  *                                                              *
#  * Solution Efficiency                                          *
#  * The user scored higher than 51.8% of users who solved this   *
#  * challenge.                                

def SwapII(s):
    s=s.swapcase()
    li=s.split(" ")
    # hàm kiểm tra chuỗi có chứa 2 số và đổi vị trí chung
    def swap(s):
        digit_positions = {}
    
    # Duyệt qua chuỗi để ánh xạ vị trí của các số
        for index, char in enumerate(s):
            if char.isdigit():
                if char not in digit_positions:
                    digit_positions[char] = index
        
        # Kiểm tra xem có ít nhất hai số trong từ điển hay không
        if len(digit_positions) != 2:
            return s
        
        # Lấy ra vị trí của các số
        positions = list(digit_positions.values())
        
        # Đổi vị trí của hai số
        index1, index2 = positions[0], positions[1]
        new_s = list(s)  # Chuyển chuỗi thành list để có thể thay đổi các phần tử
        new_s[index1], new_s[index2] = new_s[index2], new_s[index1]
        
        return ''.join(new_s)
    re=[]
    for i in li:
        re.append(i)
    return ' '.join(re)

print(SwapII("Hello -5LOL6"))       # Expected output: hELLO -6lol5
# print(SwapII("2S 6 du5d4e"))        # Expected output: 2s 6 DU4d5e
# print(SwapII("6Hello4 -8World, 7 yes3"))  # Expected output: 4hELLO6 -8wORLD, 7 YES3
# print(SwapII("a1b2c3"))             # Expected output: a1B2C3
# print(SwapII("abc123"))             # Expected output: ABC123




