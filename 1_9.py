for i in range(1,999):
    liste=[]
    a=str(i)
    if len(a)==1:
        if int(a)<9:
            liste.append(a)
            
    if len(a)==2:
        if(int(a[0])+int(a[1]))<9:
            liste.append(a)
            
    if len(a)==3:
        if (int(a[0])+int(a[1])+int(a[2]))<9:
            liste.append(a)

    for y in liste:
        print(y,end=" ")
                
