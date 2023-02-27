from django.shortcuts import render
from rest_framework import generics
from .models import Name
from .serializers import NameSerializer

# Create your views here.
class NameList(generics.ListCreateAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer

class NameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer   