from django.db import models
from django.contrib.auth.models import  User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ProcessedImageField(default='default.jpg',
                                 upload_to='profile_pics',
                                   processors=[ResizeToFill(300, 300)],
                                     format='JPEG,PNG', options={'quality': 70},
                                     blank=True, null=True
                                     )

    def __str__(self):
        return f'{self.user.username} Profile'
