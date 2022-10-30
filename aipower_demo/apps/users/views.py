from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from apps.users.serializers import RegistartionSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users import models


@api_view(['POST', ])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistartionSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            user = serializer.save()

            data['response'] = "Registration Successfully!"
            data['username'] = user.username
            data['email'] = user.email

            refresh = RefreshToken.for_user(user)
            data['token'] = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
            }
        else:
            data = serializer.errors

        return Response(data)

