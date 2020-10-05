# import our classes 
from oop_class_structure import Customer, Pet, Appointment
from datetime import datetime

# 
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
address1 = input("Enter address line 1: ")
address2 = input("Enter address line 2: ")
city = input("Enter city: ")
state = input("Enter state: ")
zip = input("Enter zip code: ")

customer1 = Customer(first_name, last_name, address1, address2, city, state, zip)
pet_name = input("Enter your pet's name: ")
breed = input("Enter your pet's breed: ")
age = int(input("Enter your pet's age: "))
pet1 = Pet(pet_name, breed, age, customer1)

begin_date =  datetime.strptime(input("Enter Start date in the format m/d/y: "), "%m/%d/%Y")
end_date = datetime.strptime(input("Enter End date in the format m/d/y: "), "%m/%d/%Y")
day_rate = float(input("Enter the day rate: "))

pet1.appointment.set_appointment(begin_date, end_date, day_rate)  

print(customer1.return_bill())

payment = float(input("Enter the payment amount: "))

customer1.make_payment(payment)

print(customer1.return_bill())
