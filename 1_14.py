liste=[]
a=121211
for i in range(1,1001):
    for j in range(1,1001):
        if i*j==121212:
            a=abs(i-j)
            liste.clear()
            liste.append([i,j])

print(liste)
            
