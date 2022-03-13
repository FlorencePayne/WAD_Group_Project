from django.db import models

#LARGE TABLES#
class Customer(models.Model):
    userID = models.CharField(max_length=8, unique=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    firstname = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    
    def __str__(self):
        return self.username

class Necklace(models.Model):
    necklaceID = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=20)
    colour = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=4)
    stock = models.IntegerField()

    
    def __str__(self):
        return self.name



#SMALLER TABLE + MAPPINGS#
class Wishlist(models.Model):
    wishlistID = models.CharField(max_length=8, unique=True)
    userID = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.wishlistID

class Wishlist_Necklace(models.Model):
    wishlistID = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    necklaceID = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    


class Cart(models.Model):
    cartID = models.CharField(max_length=8, unique=True)
    userID = models.OneToOneField(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.cartID

class Cart_Necklace(models.Model):
    cartID = models.ForeignKey(Cart, on_delete=models.CASCADE)
    necklaceID = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    quantity = models.IntegerField()



class Order(models.Model):
    orderID = models.CharField(max_length=8, unique=True)
    userID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.orderID

class Order_Necklace(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    necklaceID = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
