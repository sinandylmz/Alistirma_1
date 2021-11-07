sayı=input("Sayı giriniz:")
number=int(sayı)
for i in range(2,number):
    if number%i==0:
        print ("Asal sayı değil")
        break
else:
        print ("Asal sayı")
