class Customer:

    company_name = 'Critter Watch'

    def __init__(self, first_name, last_name, address1, address2, city, state, zip):
        self.cust_id = self.gen_id(first_name, last_name, address1)
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.balance = 0.0
        self.cust_pet = None

    def gen_id(self, first_name, last_name, address1):
        address = address1.replace(' ','')
        return f'{first_name[:3]}{last_name[:3]}{address[:5]}'

    def return_bill (self):
        return f'Customer {self.cust_id} with name {self.first_name} {self.last_name} owes ${self.balance} for {self.cust_pet.pet_name}\'s stay from {self.cust_pet.appointment.begin_date} to {self.cust_pet.appointment.end_date}'

    def make_payment(self, pmt):
        pass
    
class Pet:

    def __init__(self, name, breed, age, owner):
        self.pet_name = name
        self.breed = breed
        self.age = age
        self.appointment = None

class Appointment:

    def __init__(self, owner):
        self.begin_date = None
        self.end_date = None
        self.day_rate = 0.0
        self.total_days = 0
        self.total_cost = 0.0
        self.owner = owner

    def calc_days(self):
        pass

    def set_appointment(self, begin_date, end_date, day_rate):
        pass
