from django.urls import path
from .views import index, add_patient,add_pat

urlpatterns = [
    path('', index, name='index'),
    path('add_patient/', add_patient, name='add_patient'),
    path('add',add_pat,name='add')
]
