from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    """
    Model representing user
    """
    genderchoices = (
        ('male', 'Male'),
        ('female', 'Female'),
    )


    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    #dob = models.DateField
    gender = models.CharField(max_length=6, choices=genderchoices, default='male')
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class ReportedCases(models.Model):
    """
    Model representing reported cases
    """
    vectors = (
        ('aedes', 'Aedes Mosquito'),
        ('rat', 'Rat'),
    )

    amount = (
        ('5', '1 - 10'),
        ('18', '11 - 25'),
        ('38', '26 - 50'),
        ('75', '51 - 100'),
    )
    #case_id = models.CharField(max_length=30)
    #case_user = models.CharField(max_length=15)
    #case_date = models.DateTimeField
    #case_loc = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    case_vector = models.CharField(max_length=10, choices=vectors, default='aedes')
    case_vec_num = models.IntegerField(choices=amount, default='5')
