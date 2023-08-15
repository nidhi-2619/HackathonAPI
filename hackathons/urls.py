from . import views 
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('submissions', views.SubmissionViewSet)
router.register('hackathon-registrations', views.HackathonRegistrationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.HackathonView.as_view()),
    path('create-hackathon/',views.CreateHackathonView.as_view()),
    path('register/', views.RegisterView.as_view()),

]