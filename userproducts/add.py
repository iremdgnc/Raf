import json


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
