from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Designations, Survey, TestQuestionnaire , QuestionnaireApi

class DesignationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designations
        fields = ('id','title','text')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'title', 'text')        

class TestQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestionnaire
        fields = '__all__'        

class QuestionnaireApiSerializer(ModelSerializer):
    class Meta:
        model = QuestionnaireApi
        fields = '__all__'        
                   