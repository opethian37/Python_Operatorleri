
#1 girilen bir sayinin 0-100 arasşnda olup olmadigini kontrol ediniz.
sayi1=int(input("karsilastiirilacak sayiyi giriniz: "))
sonuc1=0<sayi1<100
print(f'sayinin 0 ile 100 arasinda olma durumu: {sonuc1}')

#2 girilen bir sayinin pozitif cift sayi olup olmadigini kontrol ediniz.
sayi2=int(input("sayiyi giriniz: "))
sonuc2=(sayi2>0) and (sayi2 %2==0)
print(f"sayi sifirdan buyuk ve 2 ye bolunebilir: {sonuc2}")

#3 kullanicidan 2 vize (%60)  ve final (%40) notu alip ortalama hesaplayin.
    #eger ortalama 50 ve ustuyse gecti degilse kaldi yazsin.
    #ortalama 50 olsa bile final notu en az 50 olmali.
    #finalden 70 alirsa ortalamanin onemi olmasin.

vize1=float(input("1.vize notu: "))
vize2=float(input("2.vize notu: "))
final=float(input("final notu: "))

sonuc=(vize1*0.3+vize2*0.3)+final*0.4
gectiBilgisi=((sonuc>=50) and (final>50 )) or (final>=70)

print(f"ogrenci gecti bilgis: {gectiBilgisi} ")

#4 kisinin ad, kilo ve boy bilgileri alinarak indeksleri hesaplayin. 
    #formül: (kilo/boy uzunlugu karesi)
    #0-18.4=zayif
    #18.5-24.9=normal
    #25.0-29.9=fazla kilolu

boy=float(input("boy giriniz: "))
kilo=float(input("kilo giriniz:"))
indeks=(kilo/(boy**2))
zayifIndeks=0<=indeks<=18.4
normalIndeks=18.5<=indeks<=24.9
fazlaKiloluIndeks=25.0<=indeks<=29.9
print(f"kisi boy/kilo indeksi: {indeks} ve zayif mi {zayifIndeks} normal mi {normalIndeks} kilolu mu {fazlaKiloluIndeks}")


