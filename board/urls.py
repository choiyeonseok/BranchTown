from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.main, name='main'),
    path('interest/', views.survey_interest, name='survey_interest'),
    path('ongoing/', views.survey_ongoing, name='survey_ongoing'),
    path('answer/', views.survey_participated, name='survey_participated'),
    path('complete/', views.survey_complete, name='survey_complete'),
    path('tag/<int:pk>/', views.survey_tag, name='survey_tag'),
]
