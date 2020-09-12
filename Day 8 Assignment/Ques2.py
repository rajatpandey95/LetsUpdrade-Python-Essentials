try:
    f=open("E:rajat.txt","r")
    f.write('HI')
    f.close()
except Exception as e:
    print(e)
