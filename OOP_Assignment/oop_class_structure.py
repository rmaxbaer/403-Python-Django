from datetime import datetime

class Customer:
    # the company is Critter Watch so all customers will be of that company
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
        self.cust_pet = None # every customer can have one and only one pet

    def gen_id(self, first_name, last_name, address1):
        # remove spaces
        address = address1.replace(' ','')

        # takes portions of each input to generate unique customer id
        return f'{first_name[:3]}{last_name[:3]}{address[:5]}'

    def return_bill (self):
        # returns a string containing inforation on what a customer owes
        start = self.cust_pet.appointment.begin_date.strftime('%m/%d/%y')
        end = self.cust_pet.appointment.end_date.strftime('%m/%d/%y')
        return f'Customer {self.cust_id} with name {self.first_name} {self.last_name} owes ${self.balance} for {self.cust_pet.pet_name}\'s stay from {start} to {end}'

    def make_payment(self, payment):
        # adjust balance when a payment is made
        self.balance -= payment

class Pet:

    def __init__(self, name, breed, age, owner):
        self.pet_name = name
        self.breed = breed
        self.age = age
        owner.cust_pet = self
        self.appointment = Appointment(owner)

class Appointment:

    def __init__(self, owner):
        self.begin_date = None
        self.end_date = None
        self.day_rate = 0.0
        self.total_days = 0
        self.total_cost = 0.0
        self.owner = owner

    def calc_days(self):
        # substract end from begin
        self.total_days = (self.end_date - self.begin_date).days

        # check if less than zero and assign 1 as base rate
        if self.total_days <= 0:
            self.total_days = 1

        # calculate total cost
        self.total_cost = self.total_days * self.day_rate

    def set_appointment(self, begin_date, end_date, day_rate):
        # assign values to variables
        self.begin_date = begin_date
        self.end_date = end_date
        self.day_rate = day_rate

        # calculate cost of appointment
        self.calc_days()

        # update customer's balance
        self.owner.balance += self.total_cost
