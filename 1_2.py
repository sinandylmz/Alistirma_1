# pi sayısının yaklaşık değerini hesaplamak
toplam=0
sayı=range(1,1000000)
for k in sayı:
    toplam=toplam+(1/k**2)
print((toplam*6)**0.5)
