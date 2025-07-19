# cyberthreat\analysis\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('analysis/', views.analysis, name='analysis'),
    path('prediction/', views.prediction, name='prediction'),
    path('model_accuracy/', views.model_accuracy, name='model_accuracy'),
    path('model_confusion_matrix/', views.model_confusion_matrix, name='model_confusion_matrix'),
]
