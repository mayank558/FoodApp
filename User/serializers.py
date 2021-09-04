from .models import User
from orders.models import Order
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','name','password']

        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def create(self, validated_data):
       password = validated_data.pop('password',None)
       instance = self.Meta.model(**validated_data)
       if password is not None:
           instance.set_password(password)
       instance.save()

       return instance

class AllOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['owner','id','title','description']
