def palo():
    sayac=0
    for i in range(100,1000):
        a=str(i)
        if int(a[0])+int(a[1])==int(a[1])+int(a[2]):
            sayac+=1
            print(a)
    print("{} tane sayı var".format(sayac))
