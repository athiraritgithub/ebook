from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from admins.models import Ebooks
from django.contrib.auth.models import User

class BookSerializers(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:

        model=Ebooks
        fields=["id","book_title","author","genres","review","favorite"]
    def create(self, validated_data):
        return Ebooks.objects.create(**validated_data)

class UserSerializer(ModelSerializer):

    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()