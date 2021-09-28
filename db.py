import json


def Merge(dict2, dict1):
    merge_dict = {**dict1, **dict2}
    return merge_dict


with open("db.JSON", "r") as file:
    data = json.load(file)
    dict1 = data


dict2 = {

        "product_id": input('Product Id Giriniz: '),
        "product_name": input('Product Name Giriniz: ')

}

print(dict1)
print(dict2)
dict3 = Merge(dict1, dict2)
print(dict3)

new_dict = json.loads(dict3)
print(new_dict)

"""file = open("db.JSON", "w")
json.dump(dict3, file)
file.close()"""