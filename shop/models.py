from django.db import models

# Create your models here.

class product(models.Model):
    product_ID = models.AutoField
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, default ="" )
    sub_category = models.CharField(max_length = 50, default ="")
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length = 200)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "shop/images", default ="")


    def __str__(self):
        return self.product_name

