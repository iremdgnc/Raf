import os
import random


def welcome_raf():
    get_id()
    while True:
        print("\nRaf'a Hoş Geldiniz.")
        a = input("- Mevcut Ürünleri Görmek İçin 'liste' Yazınız. \n- Yeni Ürün Eklemek İçin 'ekle' Yazınız. \n- "
                  "Çıkmak İçin Çıkış Yazınız. \n")
        if a == ("liste" or "Liste"):
            product_list_read()
        elif a == ("ekle" or "Ekle"):
            add_product()
        elif a == ("çıkış" or "cikis" or "Çıkış"):
            print("Programdan çıkıldı.")
            break


def get_id():
    id_list = []
    if os.path.isfile("ürünler.txt"):
        with open("ürünler.txt", "r+") as file:
            next_line = file.readline()
            while next_line != "":
                p_id = next_line.split(" ")[2]
                id_list.append(p_id)
                next_line = file.readline()
            return id_list
    else:
        return id_list


def product_list_read():
    if os.path.isfile("ürünler.txt"):
        with open("ürünler.txt", "r") as file:
            print(file.read())
    else:
        print("dosya bulunamadı")


def generate_id(array):
    limit = 10
    random_number = str(random.randint(1, limit))
    while True:
        if random_number in array:
            if len(array)==(limit):
                print("\n!!! Kapasite doldu. Kayıt yapılamaz. !!!")
                welcome_raf()
            else:
                random_number = str(random.randint(0, limit))

        if random_number not in array:
            array.append(random_number)
            return random_number


def add_product():
    products = input("Product_Name:")
    product_id = (generate_id(get_id()))
    with open("ürünler.txt", "a") as file:
        file.write(" Product_ID: " + product_id + " Product_Name: " + products + "\n")
        return file


if __name__ == '__main__':
    welcome_raf()
