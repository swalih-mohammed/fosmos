from django.urls import path
from .views import AddMemberView

app_name = 'members'

urlpatterns = [
    path('add/', AddMemberView.as_view(), name='add'),
]