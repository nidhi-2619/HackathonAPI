from django.db import models
# Create your models here.

class CreateHackathon(models.Model):
    """Model for creating Hackathon by authenticated user only"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='hackathon_images')
    hackathon_image = models.ImageField(upload_to='hackathon_images')
    # type_of_submission = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.IntegerField()

    def __str__(self):
        return self.title

class Register(models.Model):
    """Model for registering user to hackathon"""
    hackathon = models.ForeignKey(CreateHackathon, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.get_full_name()}  -   {self.hackathon.title}'

class Submission(models.Model):
    """Model for submission of hackathon"""
    hackathon = models.ForeignKey(CreateHackathon, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='hackathon_submissions')
    submission_date = models.DateTimeField(auto_now_add=True)
    is_winner = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.get_full_name()}  -   {self.hackathon.title}'