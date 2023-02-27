from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Name , Questionnaire

class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id','title','text')

class QuestionnaireSerializer(ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'
           