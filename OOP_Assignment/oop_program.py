# import our classes
from oop_class_structure import Customer, Pet, Appointment
from datetime import datetime

# prompt user for customer info
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
address1 = input('Enter address line 1: ')
address2 = input('Enter address line 2: ')
city = input('Enter city: ')
state = input('Enter state: ')
zip = input('Enter zip code: ')

# instantiate customer object
customer1 = Customer(first_name, last_name, address1, address2, city, state, zip)

num_pets = int(input('How many pets are you registering today? '))

for i in range(num_pets):
    # prompt user for pet info
    pet_name = input('Enter your pet\'s name: ')
    breed = input('Enter your pet\'s breed: ')
    age = int(input('Enter your pet\'s age: '))

    # add pet object to customer
    customer1.cust_pets.append(Pet(pet_name, breed, age, customer1))

# instantiate appointment object
for pet in customer1.cust_pets:
    # prompt user for number of appointments for each pet
    num_appts = int(input(f'How many appointments do you want to set up for {pet.pet_name}? '))

    for appt in range(num_appts):
        # prompt user for appointment info
        begin_date =  datetime.strptime(input('Enter Start date in the format m/d/y: '), '%m/%d/%Y')
        end_date = datetime.strptime(input('Enter End date in the format m/d/y: '), '%m/%d/%Y')
        day_rate = float(input('Enter the day rate: '))

        # create the appointment and add it to the current pet
        oAppointment = Appointment(customer1)
        oAppointment.set_appointment(begin_date, end_date, day_rate)
        pet.appointments.append(oAppointment)


# show bill info
print(customer1.return_bill())

# ask for payment and update customer billing info
payment = float(input('Enter the payment amount: '))
customer1.make_payment(payment)

# show bill info
print(customer1.return_bill())
