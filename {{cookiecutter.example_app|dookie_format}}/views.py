from pip._vendor.distlib.compat import filter
from rest_framework.decorators import api_view
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# @api_view(['GET'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def test_auth_perm_api_view(request, format=None):  # request作为基恩参数
#     return Response({"code": code, "message": message, "data": data})





