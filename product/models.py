from django.db import models

# Create your models here.

CATAGORY_CHOICES = (
    ('M','Mens'),
    ('W','Womens'),
    ('A','All')
)


class ProductItem(models.Model):
    
    P_name = models.CharField(max_length=100)
    P_Qty = models.IntegerField()
    P_Price = models.FloatField(max_length=15)
    CATAGORY_CHOICES = models.CharField(max_length=1, choices=CATAGORY_CHOICES, default='A')
    P_Image = models.ImageField(upload_to='image', blank=True, null=True)
    # R1_Image = models.ImageField(upload_to='image', blank=True, null=True)
    # R2_Image = models.ImageField(upload_to='image', blank=True, null=True)
    P_Desc = models.CharField(max_length=1000)
    # P_Discount = models.FloatField(max_length=15)
    #customer_id = models.ForeignKey('Customer',on_delete=models.CASCADE)
    
    def get_image_url(self):
        return f"{self.P_Image.url}"
    
    def get_image_url(self):
        return f"{self.R1_Image.url}"
    
    def get_image_url(self):
        return f"{self.R2_Image.url}"
    
    def __str__(self):
        return f"{self.P_name}"
    


    