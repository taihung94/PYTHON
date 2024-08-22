def NumberSearch(st):
    sum=0
    for i in str(st):
        if i.isdigit(): 
            sum+=int(i)
    count=0
    for i in str(st):
        if i.isalpha() : count+=1

    if count==0: return 0
    return round(sum/count)     

print(NumberSearch("Hello6 9World 2, Nic8e D7ay!"))  # Expected output: 2
print(NumberSearch("H3ello9-9"))                     # Expected output: 4
print(NumberSearch("One Number*1*"))                 # Expected output: 0
print(NumberSearch("123abc"))                        # Expected output: 1
print(NumberSearch("a1b2c3"))                        # Expected output: 2
print(NumberSearch("No numbers here!"))              # Expected output: 0   