import json
import os
import csv


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
    with open("product.json", "r") as file:
        product_list = json.load(file)

    while True:
        # Prepare user inputs
        user_input = {
            "Product__ID": input("Product ID: "),
            "Product_Name": input("Product Name: "),
            "Product_Type": input("Product Type: "),
            "Product_Color": input("Product Color: "),
            "Product_Quantity": input("Product Quantity: ")
        }
        product_list['products'].append(user_input)

        exit_adding = input("Çıkış yapmak için -1 yazınız. Ürün eklemeye devam etmek için ENTER'a basınız.")
        if exit_adding == "-1":
            print("Çıkış yapılıyor.")
            break

    with open("product.json", "w") as file:
        json.dump(product_list, file)

    return file


def user_delete_product():
    delete_id = input("Silmek İstediğiniz Ürüne Ait Product_Id Giriniz: ")
    with open("product.json", "r") as file:
        list = json.load(file)

    for i in list['products']:
        if i['Product_ID'] == str(delete_id):
            print(i)
            my_item = i

    delete = list['products'].index(my_item)  # delete_item_index
    list['products'].pop(delete)
    print(list['products'])


def user_edit_product():
    edit_id = input("Bilgilerini Düzenlemek İstediğiniz Ürüne Ait ID'yi Giriniz: ")
    edit_information = input("Hangi Bilgiyi Değiştirmek İstiyorsunuz? ")
    if edit_information == "ID":
        while True:
            print("Hatalı Giriş. ID değiştirilemez!")
            edit_information = input("Hangi Bilgiyi Değiştirmek İstiyorsunuz? ")
            if edit_information != "ID" and edit_information != "id":
                break
    new_information = input("Yeni Bilgiyi Giriniz: ")

    with open('product.json', 'r') as json_file:
        data = json.load(json_file)
        for element in data["ID"]:
            if edit_id in element:
                data[edit_information] = new_information
                print(data[edit_information])
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
    with open('product.json') as json_file:
        product_list = json.load(json_file)
        product_dict = product_list['products'][0]
        print(product_dict.keys())
        field_names = []
        for values in product_dict:
            field_names.append(values)
        print(field_names)

    with open('products.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(product_list['products'])


user_save_csv()
