from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('MRICreate/', views.MRI_create, name='MRICreate'),
    path('MRI/', views.MRI_list, name='MRIList'),
]
