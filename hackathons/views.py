from . import models
from django.contrib.auth import get_user_model, user_logged_in
from rest_framework import viewsets, generics, status
from rest_framework_jwt.utils import jwt_payload_handler
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from . import serializers
import jwt
from django.conf import settings

class HackathonViewSet(viewsets.ModelViewSet):
    queryset = models.Hackathon.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.HackathonSerializer

    class Meta:
        model = models.Hackathon
        fields = '__all__'

    def create(self, request):
        serializer = serializers.HackathonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = models.Submission.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.SubmissionSerializer


class HackathonRegistrationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.HackathonRegistration.objects.all()
    serializer_class = serializers.HackathonRegistrationSerializer
    permission_classes = [IsAuthenticated]
    user = get_user_model()

    class Meta:
        model = models.HackathonRegistration
        fields = ['user', 'hackathon']

    @action(detail=False, methods=['GET'])
    def my_registered_hackathons(self, request):
        registered_hackathons = models.HackathonRegistration.objects.filter(user=request.user)
        return registered_hackathons

    @action(detail=False, methods=['GET'])
    def my_submissions(self, request,pk=None):
        user = request.user
        try:
            enrollment = models.HackathonRegistration.objects.get(pk=pk, user=user)
            submission = enrollment.submission
            serializer = serializers.SubmissionSerializer(submission)
            return Response(serializer.data)
        except models.HackathonRegistration.DoesNotExist:
            return Response(status=404, data={"message": "No submission found for this hackathon."})

class RegisterView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer

class LoginView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.LoginSerializer
