from django.db import models
from django.contrib.auth.models import User
import random
from django.utils import timezone
from ckeditor.fields import RichTextField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    username=models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_code(self):
        self.verification_code = ''.join(random.choices('0123456789', k=6))
        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.verification_code}"
    
class PasswordResetCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    expired_at = models.DateTimeField()
    def is_valid(self):
        return timezone.now() <= self.expired_at
    
class Service(models.Model):
    name=models.CharField(max_length=100,verbose_name="Xidmətin adı")
    icon=models.FileField(null=True,blank=True,verbose_name="İkonu")
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    description=RichTextField(max_length=500,verbose_name="Açıqlama")