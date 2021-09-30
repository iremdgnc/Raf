import json


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
