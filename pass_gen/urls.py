from django.urls import path
from pass_gen import views

urlpatterns = [
    path('', views.main, name='pass_main'),
    path('pass_gen/', views.password, name='pass_gen'),
]
