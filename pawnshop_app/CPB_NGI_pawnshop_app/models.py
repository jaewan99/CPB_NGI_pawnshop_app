from django.db import models

# Create your models here.

class branch(models.Model):
   branch_name = models.CharField(max_length=100)
   branch_address= models.CharField(max_length=100, blank=True)
   branch_password = models.CharField(max_length=100)
   objects = models.Manager()

   def __str__(self):
      return super().__str__()


class customer_test(models.Model):
   customer_name = models.CharField(max_length=100)
   
   objects = models.Manager()
   def __str__(self):
      return super().__str__()