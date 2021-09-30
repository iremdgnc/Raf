import os
import random


def welcome_raf():
    print("\nRaf'a Hoş Geldiniz.")
    while True:
        print("\nHangi İşlemi Yapmak İstersiniz? ")
        user_request = input("- Mevcut Ürünleri Görmek İçin 'liste' Yazınız. \n- Yeni Ürün Eklemek İçin 'ekle' "
                             "Yazınız. \n- Bir Ürün Silmek İçin 'sil' Yazınız.  \n- Çıkmak İçin Çıkış Yazınız. \n")
        if user_request == ("liste" or "Liste"):
            product_list()
        elif user_request == ("ekle" or "Ekle"):
            add_product()
        elif user_request == ("sil" or "Sil"):
            delete_product()
        elif user_request == ("çıkış" or "cikis" or "Çıkış"):
            print("Programdan çıkıldı.")
            break


def menu():
    while True:
        user_new_request = input(
            "- Mevcut Ürünleri Görmek İçin 'liste' Yazınız. \n - Bir Ürün Silmek İçin 'sil' Yazınız.  \n- "
            "Çıkmak İçin Çıkış Yazınız. \n")
        if user_new_request == ("liste" or "Liste"):
            product_list()
        elif user_new_request == ("sil" or "Sil"):
            delete_product()
        elif user_new_request == ("çıkış" or "cikis" or "Çıkış"):
            print("Programdan çıkıldı.")
            break


def get_product_id():
    product_id_list = []
    if os.path.isfile("ürünler.txt"):
        with open("ürünler.txt", "r+") as file:
            next_line = file.readline()
            while next_line != "":
                p_id = next_line.split(" ")[2]
                product_id_list.append(p_id)
                next_line = file.readline()
            return product_id_list
    else:
        return product_id_list


def product_list():
    if os.path.isfile("ürünler.txt"):
        with open("ürünler.txt", "r") as file:
            print(file.read())
    else:
        print("Dosya Bulunamadı")


def generate_product_id(array):
    range_limit = 10
    random_number = str(random.randint(1, range_limit))
    while True:
        if random_number in array:
            if len(array) == range_limit:
                print("\n!!! Kapasite doldu. Kayıt yapılamaz. !!!")
                print("Listeleme Veya Silme İşlemi Gerçekleştirebilirsiniz.")
                menu()
            else:
                random_number = str(random.randint(0, range_limit))

        if random_number not in array:
            array.append(random_number)
            return random_number


def add_product():
    product_id = (generate_product_id(get_product_id()))
    products = input("Product_Name:")
    with open("ürünler.txt", "a") as file:
        file.write(" Product_ID: " + product_id + " Product_Name: " + products + "\n")
        return file


def delete_product():
    product_list()
    delete = input("Silmek İstediğiniz Ürüne Ait Product_Id Giriniz: ")
    with open("ürünler.txt", "r+") as file:
        new_f = file.readlines()
        file.seek(0)
        for line in new_f:
            if ('Product_ID: ' + delete) not in line:
                file.write(line)
        print("Silme İşlemi Gerçekleştirildi.")
        file.truncate()


if __name__ == '__main__':
    welcome_raf()
