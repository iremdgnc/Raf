import json


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
