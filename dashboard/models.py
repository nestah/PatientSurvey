from django.db import models
# from Auth.models import Facility, Users
from datetime import datetime


# Create your models here.

#designations model
# class Designations(models.Model):
#     # name = models.CharField(max_length=100)
#     title = models.CharField(max_length=50)
#     text = models.TextField()
#     # date_added =models.DateField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title  
#     class Meta:
#         db_table = "Designations"
#         ordering = ['updated']
class Designation(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    text = models.TextField()
    # date_added =models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  
    class Meta:
        db_table = "Designation"
        ordering = ['updated']        
# survey model
class Survey(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)  


class QuestionnaireApi(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=750)
    is_Active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # number_of_questions = models.BigIntegerField(default=4)
    number_of_questions = models.BigIntegerField(default=2)
    active_till = models.DateField(datetime.now)
    target_app = models.CharField(max_length=45)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[0:50]

    class Meta :
        
        db_table = "QuestionnaireApis"
        ordering = ['-updated']
# testing
class QuestionnaireTest(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=750)
    is_Active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # number_of_questions = models.BigIntegerField(default=4)
    number_of_questions = models.BigIntegerField(default=2)
    active_till = models.DateField(datetime.now)
    target_app = models.CharField(max_length=45)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[0:50]

    class Meta :
        
        db_table = "QuestionnaireDb"
        ordering = ['-updated']
# user list

class Userlist (models.Model):
    Username = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Designation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "AllUsers"  
# resoonse model

class Responses (models.Model):
    Question = models.CharField(max_length=120)
    Answer = models.CharField(max_length=100)

    class Meta :
        db_table = "Response"
