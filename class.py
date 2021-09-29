import json
import os
import pandas as pd


class Product:
    def __init__(self, product_id, product_name, product_type, product_color, product_quantity):
        self.product = product_id, product_name, product_type, product_color, product_quantity

    def product_name(self):
        return self.product_name()

    def product_type(self):
        return self.product_type()

    def product_color(self):
        self.product_color()

    def product_quantity(self):
        self.product_quantity()


def user_add_product():
    # get user inputs
    # ! boş veya space de benden yeniden veri girmemi iste

    with open("product.json", "r") as file:
        product_list = json.load(file)

    while True:
        # Prepare user inputs
        user_input = {
            "Product_ID": input("Product ID: "),
            "Product_Name": input("Product Name: "),
            "Product_Type": input("Product Type: "),
            "Product_Color": input("Product Color: "),
            "Product_Quantity": input("Product Quantity: ")
        }
        product_list['products'].append(user_input)

        cikis = input("Çıkış yapmak için -1 yazınız. Ürün eklemeye devam etmek için ENTER'a basınız.")
        if cikis == "-1":
            print("Çıkış yapılıyor.")
            break

    with open("product.json", "w") as file:
        json.dump(product_list, file)

    return file


def user_delete_product():
    delete_id = input("Silmek İstediğiniz Ürüne Ait Product_Id Giriniz: ")
    with open("product.json", "r") as file:
        liste = json.load(file)

    for i in liste['products']:
        if i['Product_ID'] == str(delete_id):
            print(i)
            my_item = i

    delete = liste['products'].index(my_item)  # delete_item_index
    liste['products'].pop(delete)
    print(liste['products'])


user_delete_product()


def user_edit_product():
    edit_id = input("Bilgilerini Düzenlemek İstediğiniz Ürüne Ait ID'yi Giriniz: ")
    edit = input("Hangi Bilgiyi Değiştirmek İstiyorsunuz? ")
    if edit == "ID":
        while True:
            print("Hatalı Giriş. ID değiştirilemez!")
            edit = input("Hangi Bilgiyi Değiştirmek İstiyorsunuz? ")
            if edit != "ID" and edit != "id":
                break
    edit2 = input("Yeni Bilgiyi Giriniz: ")

    with open('product.json', 'r') as json_file:
        data = json.load(json_file)
        for element in data["ID"]:
            if edit_id in element:
                data[edit] = edit2
                print(data[edit])
                break


def user_list_product():
    if os.path.isfile("product.json"):
        with open('product.json', 'r') as json_file:
            data = json.load(json_file)
            print(data)
        return json_file
    else:
        print("Dosya bulunamadı.")


def user_save_csv():
    df = pd.read_json(r'product.json')
    df.to_csv(r'products.csv', index=None)
