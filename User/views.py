from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import UserSerializer,AllOrderSerializer
from orders.models import Order
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import BasePermission,IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=serializer.data['email'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'user':serializer.data,
            'message':'user_created',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            })

class LoginView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed("User not found!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password!")
        
        return Response({
            'message':'logged_in'
        })

class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        data=User.objects.filter(id=user.id).first()
        serializer = UserSerializer(data)
        return Response(serializer.data)

class AllOrders(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AllOrderSerializer
    def get_queryset(self):
        return Order.objects.all()