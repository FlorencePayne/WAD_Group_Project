import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Floppabunny.settings')

import django
django.setup()

from floppa.models import Customer, Necklace, Wishlist, Cart, Order
from django.contrib.auth.models import User

def populate():
    
    customers = [
        {'username': 'customer1',
        'password':'123password',
        'email': 'customer1@gmail.com',
        'firstname': 'Cust',
        'surname': 'Omer1',
        'address1': '20',
        'address2': 'House Street',
        'postcode': 'G12 8QQ'
        },
        {'username': 'customer2',
        'password':'123password',
        'email': 'customer2@gmail.com',
        'firstname': 'Cust',
        'surname': 'Omer2',
        'address1': '21',
        'address2': 'House Street',
        'postcode': 'G12 8QW'
        }]

        
    necklaces = [
        {'name': 'necklace1',
        'colour':'blue',
        'description': 'pretty blue necklace',
        'price': '£10',
        'stock': 5,
        },
        {'name': 'necklace2',
        'colour':'red',
        'description': 'cooler red necklace',
        'price': '£12',
        'stock': 3,
        }]
                
 
    for necklace_data in necklaces:
        add_necklace(necklace_data)
        
        
 
    #for c in Category.objects.all():
        #for p in Page.objects.filter(category=c):
            #print(f'- {c}: {p}')
            

def add_customer(customer_data):
    cust = Customer.objects.create(username = customer_data['username'])[0]
    print(customer_data['password'])
    cust.password= customer_data['password']
    cust.email = customer_data['email']
    cust.firstname = customer_data['firstname']
    cust.surname = customer_data['surname']
    cust.address1 = customer_data['address1']
    cust.address2 = customer_data['address2']
    cust.postcode = customer_data['postcode']
    cust.save()
    
def add_necklace(necklace_data):
    neck = Necklace.objects.get_or_create(name = necklace_data['name'], description = necklace_data['description'])[0]
    neck.colour = necklace_data['colour']
    neck.description = necklace_data['description']
    neck.price = necklace_data['price']
    neck.stock = necklace_data['stock']
    neck.save()

    
if __name__ == '__main__':
    print('Starting Floppa population script...')
    populate()