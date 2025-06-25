class Car:
    def __init__(self,color,type,brand,customer_name):
        self.color=color
        self.type=type
        self.brand=brand
        self.client_name=customer_name
    
    def getMessage(self):
        print(self.client_name +" has bought "+self.type+" car of "+self.color+" color of brand "+self.brand)

c=Car("Black","Sedan","Mahindra","Himanshu")
c.getMessage()