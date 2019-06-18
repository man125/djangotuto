from django.urls import path
from . import views #same dir
from django.contrib import admin
from django.urls import include, path
app_name = 'polls'
urlpatterns = [
    path('',views.index, name ='index'),
    path('<int:question_id>/',views.detail, name ='detail'),
    path('<int:question_id>/results/',views.results, name ='results'),
    path('<int:question_id>/votes/',views.vote, name ='vote'),
]
