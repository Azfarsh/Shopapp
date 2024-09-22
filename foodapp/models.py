# foodapp/models.py
from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="No description available")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="images/", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    customer_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email_Address=models.CharField(max_length=100)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=300)
    
    def __str__(self):
        return self.Subject

