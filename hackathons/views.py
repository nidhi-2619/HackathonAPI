from .models import Hackathon, HackathonRegistration, Submission
from django.contrib.auth import get_user_model, user_logged_in, authenticate
from rest_framework import viewsets, generics, status
import jwt
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (
    HackathonSerializer,
    HackathonRegistrationSerializer,
    SubmissionSerializer,
    RegisterSerializer,
    
    
)
from django.conf import settings

User = get_user_model()

class HackathonView(generics.ListAPIView):

    queryset = Hackathon.objects.all()
    serializer = HackathonSerializer
    
    @permission_classes(AllowAny,)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = HackathonSerializer(queryset, many=True)
        return Response(serializer.data)

class CreateHackathonView(generics.CreateAPIView):
    
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticated]
    
    
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SubmissionSerializer


class HackathonRegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HackathonRegistration.objects.all()
    serializer_class = HackathonRegistrationSerializer
    permission_classes = [IsAuthenticated]
    user = get_user_model()

    class Meta:
        model = HackathonRegistration
        fields = ['user', 'hackathon']


class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    

class EnrolledHackathonListView(generics.ListAPIView):
    serializer_class = HackathonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user:
            raise {"message":"user does not exist"}
        return Hackathon.objects.filter(enrollment__user=user)

class SubmissionListView(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]
    def get(self, request, user_id=None):
        user = request.user
        try:
            enrollment = HackathonRegistration.objects.get(user=user, hackathon__id=user_id)
            submission = Submission.objects.get(enrollment=enrollment)
            serializer = SubmissionSerializer(submission)
            return Response(serializer.data)
        except HackathonRegistration.DoesNotExist:
            return Response(status=404, data={"message": "You are not enrolled in this hackathon."})
        except Submission.DoesNotExist:
            return Response(status=404, data={"message": "No submission found for this hackathon."})



