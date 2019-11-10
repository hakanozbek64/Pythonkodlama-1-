print("""***************************

Hesap Makinesi Programı

işlemler;
1.Toplama işlemi
2.Cıkarma işlemi
3.Çarpma işlemi
4.Bölme işlemi


*****************************

""")
a=int(input("Birinci sayı:"))
b=int(input("İkinci Sayı:"))

işlem=input("işlem giriniz:")

if işlem =="1":
    print("{} ile {} nin toplamı {} dir".format(a,b,a+b))
elif işlem =="2":
    print("{} ile {} nin cıkarma {} dir".format(a,b,a-b))
elif işlem =="3":
    print("{} ile {} nin çarpma {} dir".format(a,b,a*b))
elif işlem =="4":
    print("{} ile {} nin bölme {} dir".format(a,b,a/b))
else:
    print("Gecersiz İşlem.")