from django.db import models
from django.contrib.auth import get_user_model,validators,password_validation
# Create your models here.
User = get_user_model()
class Hackathon(models.Model):
    """Model for creating Hackathon by authenticated user only"""
    SUBMISSION_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon_images/')
    hackathon_image = models.ImageField(upload_to='hackathon_images/')
    type_of_submission = models.FileField(max_length=10, choices=SUBMISSION_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.IntegerField()

    def __str__(self):
        return self.title

class HackathonRegistration(models.Model):
    """Model for registering user to hackathon"""
    
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user}  -   {self.hackathon.title}'

class Submission(models.Model):
    """Model for submission of hackathon"""
    hackathon = models.ForeignKey(HackathonRegistration, on_delete=models.CASCADE,related_name='submissions')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    submission_title = models.CharField(max_length=100, blank=False, null=False, default='Submission Title')
    summary = models.TextField(blank=True, null=True, default='Summary')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    link = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='files/', blank=True, null=True)
    submission_type = models.FileField(upload_to='hackathon_submissions/',choices=Hackathon.SUBMISSION_CHOICES)

    def __str__(self):
        return f'{self.user.get_full_name()}   -   {self.hackathon.title}     -    {self.submission_title}'

