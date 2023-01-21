from django.urls import path
from . import views

# app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("charts/", views.charts, name="charts"),
    path("users/", views.users, name="users"),
    path("questionnaire/", views.questionnaires, name="questionnaire"),
    path("new-questionnaire/", views.new_questionnaire, name="new_questionnaire"),
    path('dbfetch/', views.dbfetch, name='dbfetch'),
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutuser, name='logout'),

    
    path("api/", views.DesignationsList.as_view()),
    path('<int:pk>/', views.DesignationsDetail.as_view()),
    path("api/survey", views.SurveyList.as_view()),
    path('<int:pk>/', views.SurveyDetail.as_view()),


    path('routes/', views.getRoutes),
    path('routes/api/questionnaire/', views.getQuestionnaires),
    path('routes/api/questionnaire/create/', views.CreateQuestionnaire),
    path('routes/api/questionnaire/<str:pk>/update/', views.updateQuestionnaire),
    path('routes/api/questionnaire/<str:pk>/delete/', views.deleteQuestionnaire),
    path('routes/api/questionnaire/<str:pk>/', views.getQuestionnaire)

]