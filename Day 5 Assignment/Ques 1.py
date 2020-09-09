def func(lst,sub):

    aa=len(sub)
    for i in range(len(lst)):
        if lst[i] == sub[0]:
            b=lst[i:i+aa]

            if b == sub:
                print("it's a match")
                break
    else:
        print("it's Gone")



lst = list(map(int,input('Enter the list: ').split()))
sub= list(map(int,input('Enter the sublist: ').split()))

func(lst,sub)
