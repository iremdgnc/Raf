import os
import random


def welcome_raf():
    while True:
        print("\nRaf'a Hoş Geldiniz.")
        a = input("- Mevcut Ürünleri Görmek İçin 'liste' Yazınız. \n- Yeni Ürün Eklemek İçin 'ekle' Yazınız. \n- "
                  "Çıkmak için çıkış yazınız. \n")
        if a == ("liste" or "Liste"):
            product_list_read()
        elif a == ("ekle" or "Ekle"):
            add_product()
        elif a == ("çıkış" or "cikis" or "Çıkış"):
            print("Programdan çıkıldı.")
            break

    # Raf'a hoş geldiniz yazdır. (tamam)
    # Yeni ürün eklemek için 'ekle' yazınız, (tamam)
    # Mevcut ürünler için 'liste' yazınız yazdır. (tamam)


def product_list_read():
    if os.path.isfile("ürünler.txt"):
        with open("ürünler.txt", "r") as dosya:
            print(dosya.read())
    else:
        print("dosya bulunamadı")

    # Dosya var mı kontrol et (tamam)
    # Dosya varsa dosyayı ekrana yazdır (tamam)
    # Dosya yoksa uyarı mesajı ver (tamam)
    # Dosyayı okurken ID kontrolü yap


def add_product():
    product_id = str(generate_unique_id())
    if product_id == 0:
        print('id yeri kalmadı')

    else:
        # Return Error
        products = input("Product_Name:")
        with open("ürünler.txt", "a") as file:
            file.write(" Product_ID: " + product_id + " Product_Name: " + products + "\n")
            return file

        # Kullanıcıdan product_name al (tamam)
        # Alınan her ürün için random ID ata (tamam)


def read_file():
    with open("ürünler.txt", "r+") as file:
        return file.read().splitlines()


def get_current_product_ids():
    current_product_id_array = []  # Create new array to store ids
    current_data = read_file()  # Return as array
    for i in current_data:
        current_product_id_array.append(i.split()[1])  # Get ID number of the array list

    return current_product_id_array


def generate_unique_id():
    current_ids = get_current_product_ids()  # get id number as an array
    random_number = str(random.randint(1, 2))
    for i in current_ids:
        random_number = str(random.randint(1, 2))
        if i != random_number:
            return random_number
        elif i == random_number:
            return 0

    return random_number


def _generate_id():
    id_list = []
    if os.path.isfile("ürünler.txt"):
        with open("ürünler.txt", "r+") as dosya:
            next_line = dosya.readline()
            while next_line != " ":
                p_id = next_line.split(" ")[0]
                id_list.append(p_id)
                next_line = dosya.readline()
                print(id_list)

        a = str(random.randint(0, 100))
        if a in id_list:
            new_a = str(random.randint(0, 100))
            return new_a
        else:
            return a

    else:
        print("Dosya bulunamadı")

    # dosya okuyup idleri diziye at (tamam)
    # random id al (tamam)
    # dizideki idlerle kontrol et
    # aynıysa tekrar atama yap
    # return a


# def main():


if __name__ == '__main__':
    welcome_raf()
