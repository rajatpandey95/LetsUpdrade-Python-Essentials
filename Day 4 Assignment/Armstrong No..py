for x in range(1042000,702648265):
    digit=0
    a=b=x
    while(x!=0):
        digit=digit+1
        x=x//10

    sum=0
    while(a!=0):
        rem=a%10
        a=a//10
        power=rem**digit
        
        sum=sum+power

    if b==sum:
        print('The first armstrong number is',b)
        break
