
# Exercise 2: (3 marks)
# Write a program named count_word_occurrences that reads a text file named 'data_2.txt'.
# The program counts the occurrence of each unique word, then displays the number of occurrences of each word,
# and the word with the highest frequency.
# The content of data 2.txt file:
# The quick brown fox jumps over the lazy dog.The dog was not lazy, but rather energetic.Foxes are quick and the dog is clever.
# Result:
# the: 4, quick: 2, brown: 1, fox: 1, jumps: 1, over: 1, lazy: 2, dog: 3, was: 1,not: 1, but: 1, rather: 1, energetic: 1, foxes: 1, are: 1, and 1, is: 1, clever:1
# The word ith the most frequency is 'the' which appears 4 times.
import re
def main():
    with open("data2.txt","r") as file:
        text=file.read().lower()
        text=text.replace(".","")
        text=text.replace("\n"," ")
        lines =text.split(" ")
    print(lines)
    dic={}
    for line in lines:
        if line in dic:
            dic[line]+=1
        else:
            dic[line]=1
    for k,v in dic.items():
        print(f"{k}: {v},", end=" ")
    maxcount=(max(dic.values()))
    max_re=[key for key,value in dic.items() if value == maxcount]
    result=", ".join(map(str,max_re))
    print(f"\nThe word ith the most frequency is '{result}' which appears {maxcount}")

if __name__ == "__main__":
    main()