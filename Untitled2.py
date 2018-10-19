
# coding: utf-8

# In[ ]:


print("Bu 3 yoldan birini seçiniz: ")
print("1. yol : Hipotenüs bulunacak \n ")
print("2. yol : 0 ile sizin sayınız arasındaki sayılar bulunacak \n ")
print("3. yol : gireceğiniz 6 sayının aritmetik ortalaması bulunacak \n ")

yol=float(input("izleyeceğiniz yolu seçiniz: "))       

if yol==1 :                                                    
    print("Hipotenüs hesaplanacak ...") 
    
    a=int(input("A değerini giriniz: "))
    b=int(input("B değerini giriniz"))
    c=(a**2+b**2)**0.5
    print(" hipotenüsümüz: " ,c)

elif yol==2 :                                                   
    print("0 ile sizin sayınız arasındaki sayılar bulunacak")
    d=int(input("sayı giriniz: "))
    while d>0:                                                   
        print("sayımız: ",d)
        if d == 1:
          break 
        d -= 1
    while d<0:
        print("sayımız: ",d)
        if d == 1:                                               
          break 
        d += 1
elif yol ==3:                                                       
    print("aritmetik ortalama bulunacak")
    x1=int(input("sayı giriniz: "))
    x2=int(input("sayı giriniz: "))
    x3=int(input("sayı giriniz: "))
    x4=int(input("sayı giriniz: "))
    x5=int(input("sayı giriniz: "))
    x6=int(input("sayı giriniz: "))
    cevap=(x1+x2+x3+x4+x5+x6)/6
    print("aritmetik ortalama: ",cevap)
else:
    print("sistemi yeniden başlatın...")

