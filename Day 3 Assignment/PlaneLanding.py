a=int(input('Enter the altitude: '))

if (a <= 1000):
    print("Land the Plane")
elif(a > 1000 and a <= 5000):
    print("Come down to 1000ft")
else:
    print("Go around and try later")
