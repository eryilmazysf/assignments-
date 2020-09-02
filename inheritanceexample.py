class market():
    def __init__(self,phone,address):
        self.phone=phone
        self.address=address
    def show_information(self):
        print("phone:{} \n address:{} ".format(self.phone,self.address))
    def change_adress(self,newaddress):
        self.address=newaddress
class worker(market):
    def __init__(self, id, department,sale,phone,address,):
        super().__init__(phone,address)
        self.id=id
        self.department=department
        self.sale=sale
    def raises(self,raise_amount):
        self.sale+=raise_amount
    def worker_information(self):
        print("id:{} \n department:{} \n sale:{} \n address:{}  ".format(self.id,self.department,self.sale,self.address))
class customer(market):
        def __init__(self,name,sin_no,complain,phone,address):
            super().__init__(phone,address)
            self.name=name
            self.sin_no=sin_no
            self.complain=complain

        def customer_information(self):
            print("name:{} \n sin_no:{} \n complain:{} \n address:{} ".format(self.name, self.sin_no,self.complain,self.address))
class supporter(customer):
    def __init__(self,name,id,solve,address,complain,phone):
        super().__init__(address,complain,phone)
        self.name=name
        self.id=id
        self.solve=solve
    def supporter_information(self):
        print("name:{} \n id:{} \n solve:{} \n complain:{} \n address:{}  ".format(self.name,self.id,self.solve,self.complain,self.address))
market1=market(444555,"costco")
market1.show_information()
customer1=customer("samed",12345,"bad food",444555,"costco")
customer1.show_information()
customer1.customer_information()
