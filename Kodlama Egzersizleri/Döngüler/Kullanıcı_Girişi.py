print("""********************

Kulanıcı girişi programı


**********************


""")

sys_kullanıcı_adı="hakan"
sys_parola="123456"
giriş_hakkı = 3

while True:
    kullanıcı_adı=input("Kullanıcı Adı:")
    parola= input("parola :")
    if(kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola):
        print("kullanıcı adı hatalı")
        giriş_hakkı-=1
    elif (kullanıcı_adı==sys_kullanıcı_adı and parola!=sys_parola):
        print("parola hatalı")
        giriş_hakkı-=1
    elif (kullanıcı_adı!=sys_kullanıcı_adı and parola!=sys_parola):
        print("kullanıcı adı ve parola hatalı")
        giriş_hakkı-=1
    else :
        print("sisteme başarılı bir şekilde giriş yapıldı..")
        break
    if(giriş_hakkı==0):
        print("sisteme giriş hakkınız bitti ")
        break