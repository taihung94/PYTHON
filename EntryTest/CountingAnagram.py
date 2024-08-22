#  *             CODERBYTE COUNTING ANAGRAMS CHALLENGE            *
#  *                                                              *
#  * Problem Statement                                            *
#  * Have the function CountingAnagrams(str) take the str         *
#  * parameter & determine how many anagrams exist in the string. *
#  * An anagram is a new word that is produced from rearranging   *
#  * the characters in a different word.                          *
#  * For example: cars and arcs are anagrams.                     *
#  *                                                              *
#  * Your program should determine how many anagrams exist in a   *
#  * given string and return the total number.                    *
#  *                                                              *
#  * For example: "cars are very cool so are arcs and my os"      *
#  * then your program should return 2 because "cars" and "arcs"  *
#  * form 1 anagram and "so" and "os" form a 2nd anagram.         *
#  *                                                              *
#  * The word "are" occurs twice in the string but it isn't an    *
#  * anagram because it is the same word just repeated.           *
#  * The string will contain only spaces and lowercase letters,   *
#  * no punctuation, numbers, or uppercase letters.               *
#  *                                                              *
#  * Examples                                                     *
#  * Input 1: "aa aa odg dog gdo"                                 *
#  * Output 1: 2                                                  *
#  *                                                              *
#  * Input 2: "a c b c run urn urn"                               *
#  * Output 2: 1                                                  *

def CountingAnagrams(st):
    
    arr=st.split()
    # biến tất cả các từ trong mảng sắp xếp tăng dân, sau đo tìm số lần lặp lại = yêu cầu đề bài
    arr=[''.join(sorted(w)) for w in arr]
    count=0
    dic={}
    for word in arr:
        if word in dic:
            dic[word]+=1
        else: dic[word]=1
   
    for value in dic.values():
        if value >1: count+=1
    return count

st="aa aa odg dog gdo"
print(CountingAnagrams(st))
    



