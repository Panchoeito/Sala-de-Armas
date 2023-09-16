from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer, GroupSerializer
# Create your views here.

class HomeView(TemplateView):
    template_name = 'registro_movimientos/index.html'
    
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]