from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),        # Home page
    path('page2/', views.page2, name='page2'),  # Page 2
]