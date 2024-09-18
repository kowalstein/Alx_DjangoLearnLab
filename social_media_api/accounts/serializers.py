from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError('Invalid username or password')
        token = Token.objects.create(user=user)
        return{
            'user': user,
            'token': token.key
        }
