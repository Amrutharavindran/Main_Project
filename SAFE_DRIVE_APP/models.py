from django.db import models

# Create your models here.
class login_table(models.Model):
    Username= models.CharField(max_length=100)
    Password= models.CharField(max_length=100)
    type= models.CharField(max_length=60)


class user_table(models.Model):
    LOGIN= models.ForeignKey(login_table, on_delete=models.CASCADE)
    Firstname= models.CharField(max_length=100)
    Lastname= models.CharField(max_length=100)
    Gender= models.CharField(max_length=100)
    Place= models.CharField(max_length=100)
    Post= models.CharField(max_length=100)
    Pin = models.BigIntegerField()
    Dob= models.DateField()
    Phone= models.BigIntegerField()
    Email= models.CharField(max_length=100)
    Photo= models.FileField()

class ambulance_table(models.Model):
    LOGIN= models.ForeignKey(login_table, on_delete=models.CASCADE)
    Firstname= models.CharField(max_length=100)
    Lastname= models.CharField(max_length=100)
    Gender= models.CharField(max_length=100)
    Place= models.CharField(max_length=100)
    Post= models.CharField(max_length=100)
    Pin = models.BigIntegerField()
    Dob= models.DateField()
    Phone= models.BigIntegerField()
    Email= models.CharField(max_length=100)
    Photo= models.FileField()
    Id_proof = models.FileField()
    Type=models.CharField(max_length=100)
    make_model=models.CharField(max_length=100)
    vehicle_no=models.CharField(max_length=100)
    ownership=models.FileField()



class accident_table(models.Model):
    AMBULANCE=models.ForeignKey(ambulance_table, on_delete=models.CASCADE,blank=True,null=True)
    USER_ID= models.ForeignKey(user_table, on_delete=models.CASCADE)
    Date= models.DateField()
    Time= models.TimeField()
    Latitude= models.FloatField()
    Longitude= models.FloatField()
    Status= models.CharField(max_length=100)

class pothole_table(models.Model):
    USER_ID = models.ForeignKey(user_table, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()


class location_table(models.Model):
    USER_ID = models.ForeignKey(user_table, on_delete=models.CASCADE)
    Latitude = models.FloatField()
    Longitude = models.FloatField()


class Blindspot_table(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=100)
    Latitude = models.FloatField()
    Longitude = models.FloatField()


class imp_location_table(models.Model):
    Date = models.DateField()
    Name = models.CharField(max_length=100)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Description= models.CharField(max_length=100)
    photo= models.FileField()

class Complaint_table(models.Model):
    USER_ID = models.ForeignKey(user_table, on_delete=models.CASCADE)
    Date = models.DateField()
    complaint = models.CharField(max_length=100)
    Reply = models.CharField(max_length=100)

class Feedback_table(models.Model):
    USER_ID = models.ForeignKey(user_table, on_delete=models.CASCADE)
    Date = models.DateField()
    Feedback = models.CharField(max_length=100)







