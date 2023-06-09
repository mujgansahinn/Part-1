# -*- coding: utf-8 -*-
"""operatörler.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ftyxiCeSVcNzXHgr2KWSOcGnCbVlDaUq
"""

#Aritmetik operatörler
print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3**2)
print(3//2)
print(3%2)

#Toplama operatörü
print(2+3)
print(2+3+2)
sayı1=10
print(sayı1+2) #Değişken kullanarak da yapılabilir.
sayı2=14
print(sayı1+sayı2+3.5) #Farklı veri tiplerindeki sayıları ve değişkenleri kullanabiliriz.

print('Merhaba ' + 'Dünya')
metin1='Merhaba ' + 'Dünya' + ' Nasılsın?'
print(metin1)
#Karakter dizilerini birleştirmek için kullanılabilir.

#Çıkarma operatörü
print(4-1)
sayı1=4
sayı2=1
print(sayı1-sayı2)
print(3-2-5)

#Çarpma operatörü
print(5*2)
print(5*2*3)
sayı1=5
sayı2=2
print(sayı1*sayı2)

print(10*'LA')
#Bir karakter dizisini istediğimiz kadar yazdırmak için de çarpma operatörü kullanılır.

#Bölme operatörü
print(6/4)
print(45/3/2) #İşlemler soldan başlanarak sırayla yapılır.

#Kuvvet alma operatörü
print(3**2) #3ün 2.kuvveti(3 üssü 2)
#karekök almak için 1/kuvvet yapılır.
print(36**(1/2))

#Tam bölüm operatörü
print(139.00//2) #Bölüm sonucu ondalıklı sayı ise ondalıklı kısmı almaz.

#Mod alma operatörü
print(7%5) #sayının 5 ile bölümünden kalan.
print(13%2) #kalan 0 ise sayı çifttir. 1 ise tektir.

#İlişkisel Operatörler
print(3==2) #eşit mi
print(3!=2) #farklı mı
print(3>2) #büyüktür
print(3<2) #küçüktür
print(3>=2) #büyük veya eşittir
print(3<=2) #küçük veya eşittir
print('Müjgan'is'müjgan') #değerler eşit mi
print('Müjgan'is not'müjgan') #değerler farklı mı
print('kel'in'kelebek') #içeriyor mu
print('kel'not in'kelebek') #içermiyor mu

#Eşittir operatörü
print(4==3)
#İki değer birbirine eşitse True yanlışsa False değeri verir.
sayı1=4
sayı2=3
print(sayı1==sayı2) #değişkenlere atanan değerler de aynı şekilde kontrol edilir.
print(sayı1==4)

print('Müjgan'=='Müjgan')
#Küçük-büyük harf duyarlılığına dikkat edilmeli.
metin1='Müjgan'
metin2='müjgan'
print(metin1==metin2)

#Eşit değildir operatörü
print(3!=3)
sayı1=3
sayı2=2
print(sayı1!=sayı2)
#Değerler birbirine eşitse False eşit değilse True değerini verir.

print('Müjgan'!='Müjgan')
#Küçük-büyük harf duyarlılığına dikkat edilmeli.
metin1='Müjgan'
metin2='müjgan'
print(metin1!=metin2)

#Büyüktür operatörü
sayı1=5.34
sayı2=3.67
print(sayı1>sayı2)
sayı3=8.23
print(sayı1>sayı3)

#Küçüktür operatörü
sayı1=5.34
sayı2=3.67
print(sayı2<sayı1)
print(sayı1<sayı2)

print('a'<'z')
print('z'>'a')
# Karakter dizileri alfabetik olarak sıralandığında sonradan gelen ifade daha büyük olarak kabul edilir.

#Büyük eşittir / Küçük eşittir operatörleri
sayi1=3.09
sayi2=3.09
print(sayi1>=sayi2)
print(sayi1<=sayi2)
#Sayılar eşit olduğu için ikiside True değerini verir.
sayi2=4.07
print(sayi1>=sayi2)
print(sayi1<=sayi2)
#1.sayı 2.sayıdan küçük olduğu için sadece <= operatörü True değerini verir.
sayi2=2.05
print(sayi1>=sayi2)
print(sayi1<=sayi2)
#sayi2 değişkeni sayi1 den küçük olacağı için >= operatörü True değerini verir.

# is / is not operatörleri
sayı1=3
print(sayı1 is 3)
print(sayı1 is not 3)
# “==” operatörü değerlerin eşitliğini kontrol ederken “is” aynı zamanda her iki değerin aynı nesneyi referans gösterip göstermediğini kontrol eder.

print('Müjgan'is'Müjgan')
#Küçük-büyük harf duyarlılığına dikkat edilmeli.
metin1='Müjgan'
metin2='müjgan'
print(metin1 is metin2)
print(metin1 is not metin2)

#in / not in operatörü 
print('yıl' in 'yıldız') #2. karakter dizisi içinde 1. karakter dizisi var mı?
print('yıl'not in 'yıldız') #in operatörünün tam tersi sonuç verir.

#Atama operatörleri
sayı1=3   
sayı1+=2 #arttırarak atama
sayı1-=2 #eksilterek atama
sayı1*=2 #çarparak atama
sayı1/=2 #bölerek atama
sayı1**=2 #kuvvet alarak atama
sayı1//=2 #tam sayı bölerek atama
sayı1%=2 #mod alarak atama

#Arttırarak atama operatörü
sayi1=3
sayi1+=2
print(sayi1)
metin1='Merhaba '
metin1+='Dünya' #metin1=metin1+"Dünya" koduyla aynı işlevi görür.
print(metin1)

#Eksilterek atama operatörü
sayi1=3
sayi1-=2
print(sayi1)

#Çarparak atama operatörü
sayi1=3
sayi1*=2
print(sayi1)
#Aynı şekilde karakter dizilerinde de kullanabiliriz.
metin1='Merhaba '
metin1*=5 #metin1=metin1*3 koduyla aynı işlevi görür.
print(metin1)

#Bölerek atama operatörü
sayi1=3
sayi1/=2
print(sayi1)

#Kuvvet alarak atama operatörü
sayi1=3
sayi1**=2
print(sayi1)

#Tam sayı bölerek atama operatörü
sayi1=3
sayi1//=2 #Bir değişken sayıya bölündüğünde sonucun (ondalık kısmını atarak) aynı değişkene atanmasını sağlar.
print(sayi1)

#Mod alarak atama operatörü
sayi1=3
sayi1%=2 #Bir değişkenin bir sayıya bölümünden kalanın aynı değişkene atanmasını sağlar.
print(sayi1)

#Mantıksal Operatörler
#or
#and
#not

# or operatörü
#“or” operatörü “veya” anlamındadır. Belirtilen koşullardan birinin sağlanması durumunda “True” değeri verir.
sayı1=3
print(sayı1<6 or sayı1>10)

ad='Müjgan'
print(ad=='Müjgan' or 'Gülcan')

meslek='Mühendis'
print (meslek=='Öğretmen' or meslek=='Doktor')
#Meslek ünvanı Öğretmen veya Doktor olmadığı için False döndürür.
#İkiden fazla koşul için de kullanılabilir.
print (meslek=='Öğretmen' or meslek=='Doktor' or meslek=='Mühendis')
#Meslek Ünvanı Öğretmen veya Doktor veya Mühendis'ten biri ise True değerini döndürür.

# and operatörü
#Bu operatör “ve” anlamındadır. Belirtilen koşulların hepsinin sağlanması durumunda “True” değerini verir.
puan=50
print(puan>50 and puan<60)

ad='Mert'
yasi=25
print(ad=='Mert' and yasi>=20)
#Adı Mert ve yaşı en az 20 ise True değerini döndürür.

meslek='Mühendis'
askerlikDurumu='Yaptı'
isTecrubesi=1
print (meslek=='Mühendis' and askerlikDurumu=='Yaptı')
print (meslek=='Mühendis' and askerlikDurumu=='Yaptı' and isTecrubesi>=3)

# not operatörü
#Bu operatör “değil” anlamındadır. Belirtilen koşulun tersi doğruysa “True” değeri verir.
ogrenciPuan=50
print(not(ogrenciPuan<45))
print(ogrenciPuan>45)  #Yukarıdaki ifade ile aynı işlevi görür.

#Operatörlerde öncelik sırası

#Parantez içindeki işlemler her zaman öncelikli olarak yapılır.
#Çarpma ve bölme işlemleri toplama ve çıkarma işlemine göre önce yapılır.
#Aynı derecedeki operatörlerde işlem sırası önceliği soldan sağa doğrudur.
#İşlemlerde öncelik sırasını belirtmek için en iyi yöntem operatörleri parantez içinde kullanmaktır.

print((3+2)*7) #Bu işlemin sonucunu tahmin ediniz.
#Öncelikle parantez içi yapıldığında 5*7=35

print (3+2*7) #Bu işlemin sonucu kaçtır?
#Öncelikle çarpma işlemi yapıldığından 3+14=17

print (3**2*2)  #9*2=18
print (6*7/7)  #42/7=6
print (6*3/2+8/2*3) #6*3=18  18/2=9       (9+12=21)         8/2=4  4*3=12