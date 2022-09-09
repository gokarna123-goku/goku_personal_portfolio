from django.db import models

# Create your models here.

class Contact(models.Model):
    fullname = models.CharField(max_length=122)
    email =  models.CharField(max_length=122)
    phone =  models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()


    # which shows the fullname on the database instead of showing 
    # Contact object(index=> may be 1,2,3,4,5... like that) 
    # which is not really applicable for us to understand 
    def __str__(self):
        return self.fullname


# 