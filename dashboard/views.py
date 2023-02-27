from django.shortcuts import render , redirect 
import requests 
from rest_framework import generics
from .models import Designation , Survey , QuestionnaireApi , QuestionnaireTest
from .serializers import DesignationSerializer,SurveySerializer, QuestionnaireApiSerializer ,QuestionnaireTestSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import DataForm , CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers


# from rest_framework import serializers 
# auth
from django.contrib.auth.forms import UserCreationForm

# from Auth.serializer import *

# # Create your views here.
# class based views

class DesignationList(generics.ListCreateAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
class DesignationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer   
        
#for survey
class SurveyList(generics.ListCreateAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer

class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer   

#  # for questionnaire using concrete views
class QuestionnaireApiList(generics.ListCreateAPIView):
    queryset = QuestionnaireApi.objects.all()
    serializer_class = QuestionnaireApiSerializer

class QuestionnaireApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuestionnaireApi.objects.all()
    serializer_class = QuestionnaireApiSerializer   
 

@login_required(login_url='login')
def index(request):
    total = QuestionnaireApi.objects.all().count()
    active = QuestionnaireApi.objects.filter(is_Active=True).count()
    context = {'total': total, 'active':active }
    return render(request, 'dashboard/index.html', context)


def charts(request):
    return render(request, 'dashboard/charts.html')
    
def Designation(request):
    total_designations = Designation.objects.all()
    return render(request, 'dashboard/designations.html', {'Designatons':total_designations} )

# responses from db browser for sqlite
def Response(request):
    # response = serializers.serialize('python', KPResponseReport.objects.all())
    # response = .objects.all()
    # context = {'response':response}
    return render(request, 'dashboard/TableResponse.html')

@login_required(login_url='login')
def new_questionnaire(request):
    
    if request.method == 'POST' :
        post = QuestionnaireApi()
        post.name = request.POST.get('title')
        post.is_Active = request.POST.get('isActive')
        post.description = request.POST.get('description')
        post.active_till = request.POST.get('active_till')
        post.number_of_questions = request.POST.get('number_of_questions')
        post.target_app =  request.POST.get('target_app')
        
        post.save()
        return HttpResponse('Database updated successfully with New Questionnaire')
           
    return  render(request, "dashboard/new_questionnaire.html")
       
    
def users(request):
    total_users = User.objects.all()
    staff = User.objects.filter(is_staff=True)
    date_joined = request.user.date_joined
    date_joined.strftime("%d:%m:%y %H:M:S")
    # context = {'Users': total_users}
    return render(request, "dashboard/users.html" , {'Users':total_users , 'staff':staff} )

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

def sample(request):
    return render(request, "dashboard/sample.html")

@login_required(login_url='login')
def questionnaires(request):
    total = QuestionnaireApi.objects.all().count()
    post = QuestionnaireApi.objects.all()
    context = {'QuestionnaireApis': post,'total': total }
   
    if request.method == 'POST' :
      
        name = request.POST.get['title']                      
        is_Active = request.GET['isActive']
        active_till = request.GET['active_till'] 
        number_of_questions = request.GET['number_of_questions'] 
        target_app = request.GET['target_app']                     

        
    return render(request, "dashboard/questionnaires.html", context)

