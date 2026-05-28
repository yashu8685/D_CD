from django.db import models

# Create your models here.
class student(models.Model):
    sid=models.IntegerField(unique=True)
    sname=models.CharField(max_length=20)
    smark=models.FloatField()

    sub=[
        ('MATH','MATH'),
        ('PHY','PHY'),
        ('CHE','CHE')
    ]

    ssub=models.CharField(max_length=20,choices=sub)

