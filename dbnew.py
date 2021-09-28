import json

def get_json_data():
    with open("db.JSON", "r") as file:
        data = json.load(file)

    return data


def get_element_by_name(name):
    with open("db.JSON", "r") as file:
        data = json.load(file)

    for i in data[name]:
        print(i)




if __name__ == "__main__":
    get_element_by_name('product_name')