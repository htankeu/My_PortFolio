from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('project/<str:pk>/', views.projectPage, name="project"),
    path('addProject/', views.addProject, name="add-project"),
    path('editProject/<str:pk>/', views.editProject, name="edit-project"),
    path('inbox/', views.inboxPage, name="inbox"),
    path('message/<str:pk>/', views.messagePage, name="message"),
]