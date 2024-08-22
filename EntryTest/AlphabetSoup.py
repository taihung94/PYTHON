def AlphabetSoup(s):
    # Convert the string into a list of characters
    char_list = list(s)
    
    # Sort the list of characters
    char_list.sort()
    
    # Join the sorted list back into a string
    sorted_str = ''.join(char_list)
    
    return sorted_str

# Test cases
print(AlphabetSoup("coderbyte"))  # Expected output: bcdeeorty
print(AlphabetSoup("hooplah"))    # Expected output: ahhloop
print(AlphabetSoup("hello"))      # Expected output: ehllo
print(AlphabetSoup("python"))     # Expected output: hnopty
print(AlphabetSoup("alphabet"))   # Expected output: aabehlpt
