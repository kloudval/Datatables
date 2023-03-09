from django.db import models


class Employee(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    occupation = models.CharField(max_length=100)
    salary = models.IntegerField()
    gender = models.CharField(max_length=1, null=True, choices=GENDER)

    def __str__(self):
        return self.name
