from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .serializers import UserSerializer, UserCreateSerializer
from .models import CustomUser


@api_view(['GET', 'POST'])
def users(request: HttpRequest, format=None) -> Response:
    if request.method == 'GET':
        user = request.user
        if user.is_superuser:
            users = CustomUser.objects.all()
            serializer = UserCreateSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer = UserSerializer(instance=serializer.instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
# def me(request: Request, format=None) -> Response:

#     if request.method == 'GET':
#         serializer = UserSerializer(instance=request.user)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = UserSerializer(request.user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
