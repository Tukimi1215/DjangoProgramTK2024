from django.urls import path
from. import views
from .views import nippoListView

urlpatterns = [
    path('', views.index, name='index'),
]