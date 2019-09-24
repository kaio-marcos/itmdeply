from django.urls import path, include
from meusistema.views import index

urlpatterns = [
    path('',    index)
]