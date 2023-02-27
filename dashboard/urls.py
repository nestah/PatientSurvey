from django.urls import path
from . import views

# app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("charts/", views.charts, name="charts"),
    path("users/", views.users, name="users"),
    path("questionnaire/", views.questionnaires, name="questionnaire"),
    path("new-questionnaire/", views.new_questionnaire, name="new_questionnaire"),
    path('designations/', views.Designation, name='designation'),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('sample-response', views.sample, name="sample-response"),
    path('response/', views.Response, name='response'),

    
    path("api/", views.DesignationList.as_view()),
    path('<int:pk>/', views.DesignationDetail.as_view()),
    path("api/survey", views.SurveyList.as_view()),
    path('<int:pk>/', views.SurveyDetail.as_view()),
   
    # generic api view routes
    path('qnapi/',views.QuestionnaireApiList.as_view()),
    path('qnapi/<int:pk>/', views.QuestionnaireApiDetail.as_view()),
   

]