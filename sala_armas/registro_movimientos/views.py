from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = 'registro_movimientos/index.html'
    