class Common:
    def __init__(self,product_id,product_name):
        self.product_id = product_id
        self.product_name = product_name


class Products(Common):
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

