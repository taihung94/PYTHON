def num(st):
    def sum_st(n):
        return sum(int(char) for char in str(n) )
    
    count=0
    
    while st>=10:
        st=sum_st(st)
        count+=1
    return count


print(num(14))



    
        
    