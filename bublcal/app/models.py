from django.db import models


# Create your models here.
class UserLogin(models.Model):
    user_name = models.CharField(max_length=64, primary_key=True)
    email = models.ForeignKey('UserData', on_delete=models.CASCADE)
    # email = models.CharField(max_length=64) - Not sure if foreign key is working, leaving this if needed
    password = models.CharField(max_length=64)


class UserData(models.Model):
    email = models.CharField(max_length=64, primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    time_zone = models.IntegerField()
    retention_date = models.DateField()


class BublTemplate(models.Model):
    task_id = models.CharField(max_length=256, primary_key=True)
    email = models.ForeignKey('UserData', on_delete=models.CASCADE)
    # email = models.CharField(max_length=64) - Not sure if foreign key is working, leaving this if needed
    task_name = models.CharField(max_length=64)
    bubl_template = models.JSONField()


class BublSchedule(models.Model):
    email = models.ForeignKey('UserData', on_delete=models.CASCADE)
    # email = models.CharField(max_length=64) - Not sure if foreign key is working, leaving this if needed
    schedule = models.JSONField()


class BublMonthSchedule(models.Model):
    email = models.ForeignKey('UserData', on_delete=models.CASCADE)
    # email = models.CharField(max_length=64) - Not sure if foreign key is working, leaving this if needed
    month = models.IntegerField
    week_bubl = models.JSONField()
    month_bubl = models.JSONField()
