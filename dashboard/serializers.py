from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Designation, Survey, QuestionnaireApi,  QuestionnaireTest


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ('id','name','title','text')

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'title', 'text')        


class QuestionnaireApiSerializer(ModelSerializer):
    class Meta:
        model = QuestionnaireApi
        # fields = ('name','description','active_till','is_Active','number_of_questions', 'target_app')  
        fields = '__all__'


class  QuestionnaireTestSerializer(ModelSerializer): 
    class Meta:
        model =  QuestionnaireTest
        fields = '__all__'


 
   
