from django.db import models
<<<<<<< Updated upstream
from django.contrib.auth.models import User


#LARGE TABLES#
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
=======
from random import randint

#LARGE TABLES#
class Customer(models.Model):
    userID = models.AutoField(max_length=8, primary_key=True, default= randint(0, 1000), unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40, unique=True)
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
>>>>>>> Stashed changes
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username


class Necklace(models.Model):
    name = models.CharField(max_length=20)
    colour = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=4)
    stock = models.IntegerField(default = 0)
 
    def __str__(self):
        return self.name



#SMALLER TABLE + MAPPINGS#
class Wishlist(models.Model):
    userID = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.wishlistID

class Wishlist_Necklace(models.Model):
    wishlistID = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    necklaceID = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    


class Cart(models.Model):
<<<<<<< Updated upstream
    userID = models.OneToOneField(Customer, on_delete=models.CASCADE)
=======
    cartID = models.AutoField(max_length=8, primary_key=True, unique=True)
    userID = models.ForeignKey(Customer, to_field="userID", db_column="userID", on_delete=models.CASCADE)
>>>>>>> Stashed changes
    
    def __str__(self):
       return self.cartID

class Cart_Necklace(models.Model):
    cartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    necklaceID = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)



class Order(models.Model):
    userID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.orderID

class Order_Necklace(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    necklaceID = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)
    
