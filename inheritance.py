# multilevel inheritance 

class Product:
    flat_discount = 0 
    shipping_charges = 40 
    def __init__(self,name,actual_cost,rating,brand,discount_cost):
        self.name = name 
        self.actual_cost = actual_cost 
        self.rating = rating 
        self.brand =  brand 
        self.discount_cost = discount_cost 
        self.saved_cost = actual_cost - discount_cost

    def show_product_details(self):
        print(f'Product name    : {self.name}')
        print(f'Product brand   : {self.brand}')
        print(f'Actual cost     : {self.actual_cost} /-')
        print(f'Discount price  : {self.discount_cost} /-')
        print(f'Rating          : {self.rating}')
        print(f'You saved       : {self.actual_cost -self.discount_cost} /-')
    

    def get_price(self):
        return self.discount_cost


class Bag(Product):
    def __init__(self,name,actual_cost,rating,brand,discount_cost,warranty):
        super().__init__(name,actual_cost,rating,brand,discount_cost)
        self.warranty = warranty 

    def show_product_details(self):
        super().show_product_details()
        print(f'warranty period : {self.warranty} Years') 
        print()

product1 = Bag("Bag",3000,4.0,"American Tourister",2500,3)
product1.show_product_details()

class Electronics(Product):
    def __init__(self,name,actual_cost,rating,brand,discount_cost,warranty,power):
        super().__init__(name,actual_cost,rating,brand,discount_cost)
        self.warranty = warranty 
        self.power = power 

    def show_product_details(self):
        super().show_product_details()
        print(f'Power Rating    : {self.power} watts')
        print(f'warranty period : {self.warranty} Years') 

trimmer = Electronics("Trimmer",2000,4.0,"panasonic",1800,3,100)
trimmer.show_product_details()


class Laptop(Electronics):
    def __init__(self,name,actual_cost,rating,brand,discount_cost,warranty,power,ram,ssd,os,processor):
        super().__init__(name,actual_cost,rating,brand,discount_cost,warranty,power)
        self.ram = ram 
        self.ssd = ssd 
        self.os = os 
        self.processor = processor

    def show_product_details(self):
        super().show_product_details()
        print(f'Ram             : {self.ram} gb')
        print(f'SSD             : {self.ssd} gb') 
        print(f'OS              : {self.os}')
        print(f'Processor       : {self.processor}')


l1 = Laptop("Laptop",45000,3.8,"Asus",43000,1,60,8,500,"Windows 11","Intel i5")
l1.show_product_details()

