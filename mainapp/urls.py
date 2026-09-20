from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/contact/', views.contact_ajax, name='contact_ajax'),
    path('project/<int:pk>/', views.project_detail, name='project_detail')
]