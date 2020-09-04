lst = [1, 2, 3 ,5]
lst2=['Hello','Hell',8,4]

print(len(lst))     

lst.append('Rajat')   # append
print(lst)

lst.insert(1,"ram")  # insert
print(lst)

lst.pop(5)    #pop
print(lst)

lst.extend(lst2)      #extends
print(lst)

lst.remove('ram')   #remove
print(lst)
