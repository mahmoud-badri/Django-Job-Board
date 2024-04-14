from django.urls import path
from .views import *

urlpatterns = [
    path('', job_list, name='job_list'),  # URL for the job list view
    path('<int:id>/', job_detail, name='job_detail'),  # URL for the job detail view
]
