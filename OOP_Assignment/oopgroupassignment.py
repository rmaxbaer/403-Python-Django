class Customer:
    company_name = "Critter Watch"
    def __init__(self, first_name, last_name, address1, address2, city, state, zip):
        self.cust_id = ""
        self.first_name = ""
        self.last_name = ""
        self.address1 = ""
        self.address2 = ""
        self.city = ""
        self.state = ""
        self.zip =""
        self.balance = 0.0
        self.cust_pet = None
    def gen_id(self, first_name, last_name, address1) :
        pass
    def return_bill (self) :
        pass
    def make_payment(self, pmt) :
        pass
    
