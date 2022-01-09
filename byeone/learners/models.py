from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    Roll_no = models.CharField(max_length=30, primary_key=True)
    Name = models.CharField(max_length=255)
    Class = models.CharField(max_length=255)
    School = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=12)
    Address = models.CharField(max_length=255)

    def __str__(self):
        return self.Roll_no

    class Meta:
        db_table = "Students"


class Students_Academics(models.Model):
    Students = models.ForeignKey(Students, on_delete=models.CASCADE)
    Maths = models.IntegerField()
    Physics = models.IntegerField()
    Chemistry = models.IntegerField()
    Biology = models.IntegerField()
    English = models.IntegerField()

    class Meta:
        db_table = "Students_Academics"
