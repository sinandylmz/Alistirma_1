def pallindromik():
    sayac=0
    for i in range(1000,10000):
        a=str(i)
        if str(a[0])>str(a[3]):
            sayac+=1
    return(sayac)
