import string
import random

## şifre oluşturulacak karakterler
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## kullanicidan olusturulacak parolanin uzunluk  bilgisi

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("lutfen sayi gireniz ")
        generate_random_password()

    ## karakterleri karıştırma
    random.shuffle(characters)

    ## yukarda kullanicinin belirledigi uzunluk kadar dongu calistirip karakter degiskenin icerisinden random karakter
    ## secilip password listesine atiliyor
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## karakterleri karıştırma
    random.shuffle(password)

    ## listeyi stringe ceiviriyorum
    ## listeyi yazdırma
    print("".join(password))


## invoking the function
generate_random_password()
