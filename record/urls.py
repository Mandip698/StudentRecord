import imp
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('delete/<id>',views.delete, name='delete'),
    path('update/<id>',views.update, name='update'),
]
