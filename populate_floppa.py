import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Floppabunny.settings')

import django
django.setup()

from floppa.models import Customer, Necklace, Wishlist, Cart, Order

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
        }
        {'username': 'customer3',
        'password':'123password',
        'email': 'customer3@gmail.com',
        'firstname': 'Cust',
        'surname': 'Omer3',
        'address1': '22',
        'address2': 'House Street',
        'postcode': 'G12 8QE'
        }]

    necklaces = [
        {'name': 'necklace1',
        'color':'blue',
        'description': 'oceanic blue necklace',
        'price': '£10',
        'stock': 5,
        },
        {'name': 'necklace2',
        'color':'red',
        'description': 'ruby red necklace',
        'price': '£12',
        'stock': 3,
        }
        {'name': 'necklace3',
        'color':'green',
        'description': 'emerald green necklace',
        'price': '£14',
        'stock': 6,
        }]

    for customer_data in customers:
        add_customer(customer_data)
 
    #for c in Category.objects.all():
        #for p in Page.objects.filter(category=c):
            #print(f'- {c}: {p}')
 
def add_customer(customer_data):
    cust = Customer.objects.create(username = customer_data['username'])[0]
    cust.password= customer_data['password']
    cust.email = customer_data['email']
    cust.firstname = customer_data['firstname']
    cust.surname = customer_data['surname']
    cust.address1 = customer_data['address1']
    cust.address2 = customer_data['address2']
    cust.postcode = customer_data['postcode']
    cust.save()

if __name__ == '__main__':
    print('Initiating Floppabunny population script...')
    populate()
