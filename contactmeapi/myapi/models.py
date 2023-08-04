from django.db import models
import datetime

# Create your models here.
class contactDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=80, null=False, blank=False)
    message = models.CharField(max_length=1000, null=False, blank=False)
    # saves the time in the form year-month-date whenever data is added to the table
    date = models.DateField(auto_now_add=True)

