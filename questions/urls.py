from django.urls import path
from .import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/', views.detail, name='detail'),
    path('<int:id>/update/', views.update, name='update'),

]

