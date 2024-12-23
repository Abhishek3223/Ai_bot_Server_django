from django.urls import path
from . import views

urlpatterns = [
    path('generate-script/', views.generate_script, name='generate-script'),
]
