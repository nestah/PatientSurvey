from django.urls import path
from api import views


urlpatterns = [
    path("api-view/", views.NameList.as_view()),
    path('<int:pk>/', views.NameDetail.as_view()),
    # path('routes/', views.getRoutes),
    # path('routes/api/quesionnaire/', views.getQuestionnaires),
    # path('routes/api/quesionnaire/create', views.CreateQuestionnaire),
    # path('routes/api/quesionnaire/<str:pk>/update/', views.updateQuestionnaire),
    # path('routes/api/quesionnaire/<str:pk>/delete/', views.deleteQuestionnaire),
    # path('routes/api/quesionnaire/<str:pk>/', views.getQuestionnaire)
   

]