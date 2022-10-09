import math
x=math.pi/5
n=int(input("girmek istediginiz terim="))
toplam=0
sign=1
for i in range(n):
    toplam=toplam+sign*(x**(2*i))/math.factorial(2*i)
    sign=(-1)*sign

cos_true=math.cos(x)
print("yaklasık deger",toplam)
print("cos(x) gercek degeri",cos_true)
hata=(cos_true-toplam)
print("kesme hatası=",hata)