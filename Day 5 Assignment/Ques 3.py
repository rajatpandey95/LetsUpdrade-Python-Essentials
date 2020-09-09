def fun(i):
    i=list(i.split(" "))
    return list(map(lambda x :x.capitalize(), i))


a =['hey this is sai','i am in mumbai']
l=[]
for i in a:
    l.append( fun(i))
print(list(map(lambda x:' '.join(x),l)))
