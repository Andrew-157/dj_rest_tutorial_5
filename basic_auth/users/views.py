from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .serializers import UserSerializer, UserCreateSerializer
from .models import CustomUser


# @api_view(['POST'])
# def register(request: Request, format=None) -> Response:
#     serializer = UserCreateSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(data={'message': 'Success'}, status=status.HTTP_201_CREATED)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
