x,y,z=2,5,10
sayilar=1,5,7,10,6

#1 kullanicidan alinan 2 sayinin carpimi ile x,y,z toplaminin farki nedir?
sayi1=int(input("sayi 1'i giriniz: "))
sayi2=int(input("sayi 2'yi giriniz: "))
carpim1=sayi1*sayi2
sonuc1=carpim1-(x+y+z)
print(sonuc1)

#2 y'nin x'e kalansiz bolumunu hesaplayiniz.
sonuc2=y//x 

#3 x,y,z toplaminin mod 3'ü nedir?
toplam3=x+y+z
sonuc3=toplam3%3
print(sonuc3)

#4 y'nin x'inci kuvvetini hesaplayin.
sonuc4=y**x
print(sonuc4)

#5 x,*y,z=sayilar islemine gore z'nin kupu kactir?
sayilar5=1,5,7,10,6
x,*y,z=sayilar5
print(z**3)

#6 