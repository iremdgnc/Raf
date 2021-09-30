import json
import os


def user_list_product():
    if os.path.isfile("product.json"):
        with open('product.json', 'r') as json_file:
            data = json.load(json_file)
            print(data)
        return json_file
    else:
        print("Dosya bulunamadı.")
