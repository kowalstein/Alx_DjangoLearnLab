from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'bio', 'profile_picture')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError('Invalid username or password')
        token = Token.objects.create(user=user)
        created = get_user_model().objects.create_user
        return{
            'user': user,
            'token': token.key
        }
