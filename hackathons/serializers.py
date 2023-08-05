from . import models 
from rest_framework import serializers
from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model, password_validation

User = get_user_model()
class HackathonSerializer(serializers.ModelSerializer):
    """Serializer for Hackathon"""
    class Meta:
        model = models.Hackathon
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Submission
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for User Registration"""
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[
            password_validation.validate_password
        ]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username', 'password','confirm_password')
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class HackathonRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for Particular Hackathon Registration"""
    class Meta:
        model = models.HackathonRegistration
        fields = '__all__'



