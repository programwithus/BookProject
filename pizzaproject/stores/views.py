from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer
from .models import Pizzeria
# Create your views here.


class PizzeriaListAPIView(generics.ListAPIView):
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaListSerializer

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
	lookup_field = "id"
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaCreateAPIView(generics.CreateAPIView):
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
	lookup_field = "id"
	queryset = Pizzeria.objects.all()
	serializer_class = PizzeriaDetailSerializer

class PizzeriaDestroyAPIView(generics.DestroyAPIView):
	lookup_field = "id"
	queryset = Pizzeria.objects.all()
		