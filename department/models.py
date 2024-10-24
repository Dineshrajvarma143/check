from django.db import models

# Create your models here.
class EEE(models.Model):
    ptitle=models.CharField(max_length=100)
    pmembers=models.CharField(max_length=100)
    pdescription=models.CharField(max_length=300)
    pguide=models.CharField(max_length=20)
    pdomain=models.CharField(max_length=40)
    pyear=models.ForeignKey('year',on_delete=models.CASCADE)
    def __str__(self):
        return self.ptitle


class Year(models.Model):
    pyear=models.CharField(max_length=5)
    dealHOD=models.CharField(max_length=30)
    coordinator=models.CharField(max_length=30)
    def __str__(self):
        return self.pyear

class Booking(models.Model):
    staff=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    Ryear=models.IntegerField()
    department=models.CharField(max_length=30)
    contact=models.IntegerField()
    currentrole=models.CharField(max_length=30)
    def __str__(self):
        return self.department
