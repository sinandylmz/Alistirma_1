liste=[]
for i in range (1,351):
    if 125%i==200%i==350%i:
        liste.append(i)

liste.sort()
print(liste[-1])
