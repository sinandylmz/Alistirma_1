def aynirakam():
    sayac=0
    for i in range(100,1000):
        a=str(i)
        if i%2==0 and (a[0]==a[1] or a[0]==a[2] or a[1]==a[2] or a[0]==a[1]==a[2]):
            sayac+=1
    return sayac

    
