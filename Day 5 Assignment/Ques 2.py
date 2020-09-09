def prime(a):
    for j in range(2,a):
        if(a%j==0):
            break
    else:
        return a
    
l=list(range(1,2501))

primenumbers = filter(prime,l)
print(list(primenumbers))
