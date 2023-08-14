from django.urls import path
from derma.views import DiseaseView

urlpatterns = [
    path('', DiseaseView.as_view()),
]
