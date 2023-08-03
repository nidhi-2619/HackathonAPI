from . import views 
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('hackathons', views.HackathonViewSet)
router.register('submissions', views.SubmissionViewSet)
router.register('hackathon-registrations', views.HackathonRegistrationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
]