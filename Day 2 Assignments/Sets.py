st = {1, 2, 3, 4, 8}
st1 = {7, 8, 9, 2}

st.add(45)    # add
print(st)

a=st.union(st1)    #union
print(a)

b=st.intersection(st1)   #intersection
print(b)

st.discard(45)      #discard
print(st)

aa = st.difference(st1)   #difference
print(aa)
