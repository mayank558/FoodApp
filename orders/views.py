from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import Serializer
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView
from .models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CreateOrder(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        return Response(serializer.data)


class ListOrder(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)