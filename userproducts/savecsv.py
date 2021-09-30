import json
import csv


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
