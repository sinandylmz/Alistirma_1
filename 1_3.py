toplam=0
for n in range(0,1000):
    
    fakto=1
    for t in range (1,n+1):
        fakto=fakto*t
        
    toplam+=1/fakto

print(toplam)
