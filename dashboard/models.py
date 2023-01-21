from django.db import models
# from Auth.models import Facility, Users
from datetime import datetime


# Create your models here.

#designations model
class Designations(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title  

# survey model
class Survey(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)  

class TestQuestionnaire(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=750)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_questions = models.BigIntegerField(default=4)
    active_till = models.DateField(datetime.now)
    target_app = models.CharField(max_length=45)

    class Meta:
    
        db_table = "TestQuestionnaires"    


class QuestionnaireApi(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=750)
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_questions = models.BigIntegerField(default=4)
    active_till = models.DateField(datetime.now)
    target_app = models.CharField(max_length=45)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[0:50]

    class Meta:
        db_table = "QuestionnaireApis"
        ordering = ['-updated']
                            

