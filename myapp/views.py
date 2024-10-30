from django.shortcuts import render
from .models import Student
from .serializers import studentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
class studentListCreat(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=studentSerializer

class studentReUptDes(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=studentSerializer