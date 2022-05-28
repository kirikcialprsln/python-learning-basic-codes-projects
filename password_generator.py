import string
import random

## şifre oluşturulacak karakterler (TR)
## characters to create password (EN)
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## kullanicidan olusturulacak parolanin uzunluk  bilgisi (TR)
    ## Length information of the password to be created from the user (EN)

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("lutfen sayi gireniz ")
        generate_random_password()

    ## karakterleri karıştırma (TR)
    ## mixing characters (EN)
    random.shuffle(characters)

    ## yukarda kullanicinin belirledigi uzunluk kadar dongu calistirip karakter degiskenin icerisinden random karakter secilip password listesine atiliyor (TR)
    ##After running the loop for the length determined by the user above, random character is selected from the character variable and added to the password list.(EN)
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    ## karakterleri karıştırma (TR)
    ## mixing characters (EN)
    random.shuffle(password)

    ## listeyi stringe ceiviriyorum (TR)
    ## listeyi yazdırma (TR)
    ## convert list to string (EN)
    ## ## print the list (EN)
   
    print("".join(password))

## işlevi çağırmak (TR)
## invoking the function (EN)
generate_random_password()
