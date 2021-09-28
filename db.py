import json


def get_element_by_name():
    # Open JSON
    with open("db.JSON", "r") as file:
        data = json.load(file)

    print(type(data['products']))

    user_input = {"product_id": input('Product Id Giriniz: '), "product_name": input('Product Name Giriniz: ')}
    data['products'].append(user_input)

    with open("db.JSON", "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    get_element_by_name()