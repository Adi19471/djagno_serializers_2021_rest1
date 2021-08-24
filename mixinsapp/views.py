from django.shortcuts import render

# Create your views here.
from .models import LaptopDetailes
from .serializers import LaptopDetailesSerializers

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


class Studentlist(GenericAPIView,ListModelMixin):
    queryset = LaptopDetailes.objects.all()
    serializers_class = LaptopDetailesSerializers
    def get(self,request):
        return self.list(request)