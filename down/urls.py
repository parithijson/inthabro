from . import views
from django.urls import path
urlpatterns = [
    path('', views.home),
    path('download/', views.download, name="download")
]
