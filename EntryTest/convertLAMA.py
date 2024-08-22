def BasicRomanNumerals(roman):
    # Mapping of Roman numerals to their integer values
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    length = len(roman)
    
    # Iterate through the Roman numeral string
    for i in range(length):
        # Check if this numeral should be subtracted
        if i < length - 1 and roman_to_int[roman[i]] < roman_to_int[roman[i + 1]]:
            total -= roman_to_int[roman[i]]
        else:
            total += roman_to_int[roman[i]]
    
    return total

# Test cases
print(BasicRomanNumerals("IV"))   # Expected output: 4
print(BasicRomanNumerals("XLVI")) # Expected output: 46
print(BasicRomanNumerals("XXIV")) # Expected output: 24
print(BasicRomanNumerals("MCMXC")) # Expected output: 1990
print(BasicRomanNumerals("MMVIII")) # Expected output: 2008
print(BasicRomanNumerals("IX"))   # Expected output: 9
