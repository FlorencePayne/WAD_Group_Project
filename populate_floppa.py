import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Floppabunny.settings')

import django
django.setup()

from floppa.models import Customer, Necklace, Order, Order_Necklace
from django.contrib.auth.models import User

def populate():

#all the population data. List of dictionaries, each dictionary represents new data so 3 dictionaries for customers means 3 customer.
#each field has the same name in the Models.py to avoid confusion     
    customers = [
        {'username': 'customer1',
        'password':'verysecurepassword123!',
        'email': 'customer1@gmail.com',
        'first_name': 'Cust',
        'last_name': 'Omer1',
        'address1': '20',
        'address2': 'House Street',
        'postcode': 'G12 8QQ'
        },
        {'username': 'customer2',
        'password':'verysecurepassword123!',
        'email': 'customer2@gmail.com',
        'first_name': 'Cust',
        'last_name': 'Omer2',
        'address1': '21',
        'address2': 'House Street',
        'postcode': 'G12 8QW'
        }]

        
    necklaces = [
        {'name': '333',
        'colour':'multi',
        'description': 'This necklace was inspired by the album cover for 333 by Bladee, and features recycled chain details with butterflies, metal "3" chars, glass stars, millefiori hearts&stars and faux pearls!',
        'price': '£18',
        'stock': 5,
        },
        {'name': 'Strawberry Jelly',
        'colour':'pink',
        'description': 'This necklace is as sweet as jelly and ice cream on a hot Summer day ! <3 It features faux pearls, Czech glass beads and Millefiori glass heart beads!',
        'price': '£14',
        'stock': 3,
        },
        {'name': 'Garden of Eden',
        'colour':'green',
        'description': 'This necklace was made for green loving garden fairies. It features Czech glass beads, glass stars, faux pearls, reused vintage green beads and leaf charms!',
        'price': '£14',
        'stock': 7,
        }]
        
    order = [
        {'username': 'customer1',
        'placed':False,
        },
        {'username': 'customer2',
        'placed':False,
        }]

    #compound key of orderID and NecklaceID. Necklace corresponds to name in necklaces. If you change the name there please change the name here too.
    #Same for the username. If you change it please make sure its changed in both places    
    order_necklace = [
        {'username': 'customer1',
        'name':'333',
        'quantity' : 1,
        },
        {'username': 'customer1',
        'name':'Strawberry Jelly',
        'quantity' : 2,
        },
        {'username': 'customer2',
        'name':'Garden of Eden',
        'quantity' : 1,
        }]
                
 
#all the for loops that go through our data and pass them to the functions
    for necklace_data in necklaces:
        add_necklace(necklace_data)
        
    
    for customer_data in customers:
        add_customer(customer_data)
        
    
    for order_data in order:
        add_order(order_data)
        
    for order_necklace_data in order_necklace:
        add_order_necklace(order_necklace_data)
        
 

            
#add customer script, takes in customer_data tries to find a user with the given username if it can't then it creates a new user
#had to use set_password since password wasn't being accepted.
#usermodel and customer are different models. User is a foreign key, so have to fill that in seperatly.
def add_customer(customer_data):
    usermodel = User.objects.get_or_create(username = customer_data['username'])[0]
    usermodel.set_password(customer_data['password'])
    usermodel.email = customer_data['email']
    usermodel.first_name = customer_data['first_name']
    usermodel.last_name = customer_data['last_name']
    usermodel.save() #dont forget to save!
    cust = Customer.objects.get_or_create(user = usermodel)[0] #at user field in the Customer model set it to the user we just created above
    cust.address1 = customer_data['address1']
    cust.address2 = customer_data['address2'] #address stuff
    cust.postcode = customer_data['postcode']
    cust.save() #dont forget to save!
    #since there's 2 different models we have to save individualy 

#works similar to customer one. Take in the data, try and retrieve it if it doesn't exist create it. Enter all fields and save    
def add_necklace(necklace_data):
    neck = Necklace.objects.get_or_create(name = necklace_data['name'], description = necklace_data['description'])[0]
    neck.colour = necklace_data['colour']
    neck.description = necklace_data['description']
    neck.price = necklace_data['price']
    neck.stock = necklace_data['stock']
    neck.save()
    
def add_order(order_data):
    usermodel = User.objects.get(username = order_data['username']) #we try to find the usermodel for the user ordering
    cust = Customer.objects.get(user = usermodel) #we match the usermodel to the cusmtomer model
    order = Order.objects.get_or_create(userID = cust)[0] #create order using rhe UserID
    order.placed = order_data['placed']
    order.save()
    
    
def add_order_necklace(order_necklace_data):
    neck = Necklace.objects.get(name = order_necklace_data['name']) #we get the necklace that the user wants
    usermodel = User.objects.get(username = order_necklace_data['username']) #we get the data of the user that wants it
    
    cust = Customer.objects.get(user = usermodel) #find the user so we can use their ID
    
    order = Order.objects.get(userID = cust)  #use the ID to find their order
    order_necklace = Order_Necklace.objects.get_or_create(orderID = order, necklaceID = neck)[0]  #get/create using the orderID and necklaceID we got above
    order_necklace.quantity = order_necklace_data['quantity']  #quantity
    order_necklace.save()
    

    
#starts the whole thing    
if __name__ == '__main__':
    print('Starting Floppa population script...')
    populate()