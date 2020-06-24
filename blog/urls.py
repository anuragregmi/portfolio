from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.listblogs, name="list"),
    path('<int:blog_id>/', views.detailblog, name="detail"),
]
