for i in range(10,100):
    a=str(i)
    for j in range(10,100):
        b=str(j)
        if int(a+b)==(i+j)*11:
            print(a,b)
