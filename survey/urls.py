from django.urls import path
from . import views

app_name = "survey"

urlpatterns = [
    path('make/', views.make_survey, name='make_survey'),
    path('make/<int:pk>/', views.make_index, name='make_index'),
    path('make/<int:pk>/choice/', views.make_multiple_choice, name='make_multiple_choice'),
    path('make/<int:pk>/text/', views.make_text_answer, name='make_text_answer'),

    # path('<int:pk>/multiple_choice/', views.multiple_choice, name='multiple_choice'),
    path('<int:pk>/results/', views.results, name='results'),

]
