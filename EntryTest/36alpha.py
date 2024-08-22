def AlphabetSearching(s):
    # Create a set of all letters in the English alphabet
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    
    # Initialize a dictionary to track the presence of each letter
    alphabet_dict = {letter: False for letter in alphabet_set}
    
    # Iterate through each character in the input string
    for char in s:
        # If the character is a letter, mark it as found in the dictionary
        if char.isalpha():
            alphabet_dict[char.lower()] = True
    
    # Check if all letters in the dictionary are marked as True
    return "true" if all(alphabet_dict.values()) else "false"

# Test cases
print(AlphabetSearching("zacxyjbbkfgtbhdaielqrm45pnsowtuv"))  # Expected output: true
print(AlphabetSearching("abcdefghijklmnopqrstuvwxyz"))        # Expected output: true
print(AlphabetSearching("abcdefghijklmnopqrstuvwxyyyy"))      # Expected output: false
print(AlphabetSearching("abc123456kmo"))                      # Expected output: false
print(AlphabetSearching("the quick brown fox jumps over the lazy dog"))  # Expected output: true
