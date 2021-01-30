from django.http.response import Http404
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import serializers, status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer

# Generic class-based views. Cuando se que todlas requests que se hagan van a ser simples y no necesito explayarme sobre ninguna
class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Class-based view
# De esta manera puedo controlar que se hace en cada tipo de petición
# class TaskAPIView(APIView):
#     def get(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Mixins class-based view
# Me ahorro más código con los mixins. Puedo usarlo cuando todas las requests sean simples salvo alguna que quiera explicitar
# class TaskDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)