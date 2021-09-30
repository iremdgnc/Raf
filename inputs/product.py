from inputs import common


class Products(common.Common):
    def __init__(self,product_id,product_name,color,type,quantity):
        super().__init__(product_id,product_name)
        self.color = color
        self.type = type
        self.quantity = quantity
        self.information = {
            "Product_ID": self.product_id,
            "Product_Name": self.product_name,
            "Color": self.color,
            "Type": self.type,
            "Quantity": self.quantity
        }

sayac = 0
user_inputs = list()
while True:
    user_input = Products(input("Product_Id: "), input("Product_Name: "), input("Product_Color: "), input("Product_Type: "), input("Product_Quantity: "))
    user_inputs.append(user_input.information)
    sayac += 1
    if sayac == 2:
        print(user_inputs)
        break