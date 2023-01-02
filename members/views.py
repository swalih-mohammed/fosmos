from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from .models import Member
from . forms import AddForm
from django.db.models import F
from django.utils import timezone


""" 
class AddBookView(FormView):
    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 
"""


class AddMemberView(CreateView):
    model = Member
    form_class = AddForm
    template_name = 'form.html'
    success_url = '/'