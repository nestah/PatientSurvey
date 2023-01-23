from django.shortcuts import render , redirect
from rest_framework import generics
from .models import Designations , Survey, TestQuestionnaire , QuestionnaireApi
from .serializers import DesignationsSerializer,SurveySerializer,QuestionnaireApiSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import DataForm , CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
# auth
from django.contrib.auth.forms import UserCreationForm

# from Auth.serializer import *

# Create your views here.
class DesignationsList(generics.ListCreateAPIView):
    queryset = Designations.objects.all()
    serializer_class = DesignationsSerializer

class DesignationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designations.objects.all()
    serializer_class = DesignationsSerializer   
#for survey
class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer   

 # for questionnaire
class QuestionnaireApiList(generics.ListCreateAPIView):
    queryset = QuestionnaireApi.objects.all()
    serializer_class = QuestionnaireApiSerializer

class QuestionnaireApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionnaireApi.objects.all()
    serializer_class = QuestionnaireApiSerializer   
 

@login_required(login_url='login')
def index(request):
    return render(request, 'dashboard/index.html')


def charts(request):
    return render(request, 'dashboard/charts.html')

@login_required(login_url='login')
def new_questionnaire(request):
    
    if request.method == 'POST' :
        post = QuestionnaireApi()
        post.name = request.POST.get('title')
        post.status = request.POST.get('isActive')
        post.description = request.POST.get('description')
        post.active_till = request.POST.get('active_till')
        post.num_questions = request.POST.get('number_of_questions')
        post.target_app =  request.POST.get('target_app')
        
        post.save()
        return HttpResponse('Database updated successfuly with New Questionnaire')
           
    return  render(request, "dashboard/new_questionnaire.html")
       
    
def users(request):

    return render(request, "dashboard/users.html")

def RegisterPage(request):

    if request.user.is_authenticated :
        return redirect('dashboard')
    else:
        
        form = CreateUserForm()
        context = {'form': form}    
        if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
           user = form.cleaned_data.get('username')
           messages.success(request, 'account was created successfully for ' + user )
           return redirect('login')
        #    messages.info(request, ' username or password does not exist ') 

    return render(request, 'accounts/reg_form.html', context)
def loginPage(request):
    if request.user.is_authenticated :
        return redirect('dashboard')
    else:    
        if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')

           user = authenticate(request, username=username , password=password)
           if user is not None:
                login(request, user)
           return redirect('dashboard')
        else:
                # messages.info(request, ' username or password does not exist ')   
                context = {}      
    return render(request, 'accounts/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def dbfetch(request):
    return render(request, "dashboard/dbfetch.html")

@login_required(login_url='login')
def questionnaires(request):
    post = QuestionnaireApi.objects.all()
    context = {'QuestionnaireApis': post}
    if request.method == 'POST' :
        
        name = request.POST.get['title']                      
        isActive = request.GET['isActive']
        active_till = request.GET['active_till'] 
        number_of_questions = request.GET['num_questions']                      

        
    return render(request, "dashboard/questionnaires.html", context)

# rest_framework views
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/api/questionnaire/',
            'Method': 'GET',
            'Body': None,
            'description':'returns an array of questionnaire',
        },
          {
            'Endpoint': '/api/questionnaire/id',
            'Method': 'GET',
            'Body': None,
            'description':'returns a single questionnaire object',
        },
          {
            'Endpoint': '/api/questionnaire/create',
            'Method': 'POST',
            'Body': {'body':""},
            'description':'creates a new questionnaire with data sent in the new req',
        },
          {
            'Endpoint': '/api/questionnaire/id/update',
            'Method': 'PUT',
            'Body': {'body':""},
            'description':'updates existing questionnaire specific to id',
        },
          {
            'Endpoint': '/api/questionnaire/id/delete',
            'Method': 'DELETE',
            'Body': None,
            'description':'deletes an existing questionnaire',
        }
    ]
    return Response(routes)

# get all questionnaires
@api_view(['GET'])
def getQuestionnaires(request):
        Questionnaires = QuestionnaireApi.objects.all()
        serializer = QuestionnaireApiSerializer(Questionnaires, many=True)
        return Response(serializer.data)

# get Questionnaire by id
@api_view(['GET'])
def getQuestionnaire(request, pk):
        Questionnaire = QuestionnaireApi.objects.get(id=pk)
        serializer = QuestionnaireApiSerializer(Questionnaire, many=False)
        return Response(serializer.data)

# create Questionnaire
@api_view(['POST'])
def CreateQuestionnaire(request):
     
    serializer = QuestionnaireApiSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# update Questionnaire
@api_view(['PUT'])
def updateQuestionnaire(request, pk):
    # pk = int(pk)
    Questionnaire = QuestionnaireApi.objects.get(id=pk)
    serializer = QuestionnaireApiSerializer(instance=Questionnaire, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    

# delete Questionnaire
@api_view(['DELETE'])
def deleteQuestionnaire(request, pk):
    pk = int(pk)
    questionnaire = QuestionnaireApi.objects.get(id=pk)
    questionnaire.delete()
    return Response('Questionnaire was deleted')     
        


    



    
    









