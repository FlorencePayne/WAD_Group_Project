from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


#LARGE TABLES#
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    postcode = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.username


class Necklace(models.Model):
    name = models.CharField(max_length=20, unique = True)
    colour = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    price = models.CharField(max_length=4)
    stock = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True)
    image1 = models.ImageField(null=True, blank=True, max_length=255, upload_to ="necklacePictures/")
    image2 = models.ImageField(null=True, blank=True, max_length=255, upload_to ="necklacePictures/")
 
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Necklace, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name



#SMALLER TABLE + MAPPINGS#
class Order(models.Model):
    userID = models.OneToOneField(Customer, on_delete=models.CASCADE)
    placed = models.BooleanField(default = False)
    
    def __int__(self):
       return self.id

class Order_Necklace(models.Model):
    orderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    necklaceID = models.ForeignKey(Necklace, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 0)

    