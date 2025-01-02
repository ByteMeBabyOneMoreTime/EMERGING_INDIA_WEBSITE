from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from website.utils import compress_image
from django.core.exceptions import ValidationError

def validate_image_size(image):
    max_size_kb = 200  # Max size in KB
    if image.size > max_size_kb * 1024:  # Convert KB to Bytes
        raise ValidationError(f'Image file size must be under {max_size_kb} KB.')

class User(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False)
    STATUS = (
        ('Regular', 'Regular'),
        ('Subscriber', 'Subscriber'),
        ('Moderator', 'Moderator')
    )
    email = models.EmailField(unique=True)
    email_status = models.BooleanField(default=False)
    status = models.CharField(max_length=200, choices=STATUS, default='Regular')


    # Profile Picture
    profile_picture = models.URLField(max_length=2000, default='https://drive.google.com/thumbnail?id=1eS5nP8cMj8eJ-Nq_PHTgLa7rJkj5UCPh&sz=s4000')
    
    
        

    def __str__(self) -> str:
        return f'Name: {self.first_name}, status: {self.status}, email: {self.email}'

class tokens(models.Model):
    token = models.CharField(max_length=300)
    