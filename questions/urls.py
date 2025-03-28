from django.urls import path
from .import views

app_name = 'questions'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:question_id>/comments/create', views.comment_create, name='comment_create'),
]

