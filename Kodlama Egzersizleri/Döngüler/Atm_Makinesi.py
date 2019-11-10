print("""*********************

ATM Makinesine Hoşgeldiniz.

işlemler;

1.bakiye sorgulama 

2.Para yatırma

3.Para Çekme

Programdan cıkmak için 'q'ya basınız..

*************************
""")

bakiye=1000

while True :
    işlem=input("işlemi seçiniz:")
    if(işlem=="q"):
        print("yine bekleriz...")
        break
    elif(işlem=="1"):
        print("bakiyeniz {} tl dir".format(bakiye))

    elif(işlem=="2"):
        miktar=int(input("Miktarı Giriniz:"))
        bakiye+=miktar

    elif(işlem=="3"):
        miktar = int(input("Miktarı Giriniz:"))
        if(bakiye-miktar<0):
            print("böyle bir para cekemezsiniz..")
            continue
        bakiye-=miktar

    else:
        print("gecersiz işlem")