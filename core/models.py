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
    

    # homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
class Service(models.Model):
    name=models.CharField(max_length=100,verbose_name="Xidmətin adı")
    icon=models.FileField(null=True,blank=True,verbose_name="İkonu")
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    description=RichTextField(max_length=500,verbose_name="Açıqlama")

class Serv(models.Model):
    image=models.FileField(verbose_name="Şəkil")
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    description=RichTextField(max_length=500,verbose_name="Açıqlama")

class Praise(models.Model):
    image=models.FileField(verbose_name="Şəkil")
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    description=RichTextField(max_length=500,verbose_name="Açıqlama")
    name_lastname = models.CharField(max_length=100,verbose_name="Ad və soyad")
    company = models.CharField(max_length=100,verbose_name="Şirkət")
    
class New(models.Model):
    image=models.FileField(verbose_name="Şəkil")
    category = models.CharField(max_length=100,verbose_name="Kateqoriya")
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    name_lastname = models.CharField(max_length=100,verbose_name="Ad və soyad")
    icon = models.FileField(verbose_name="Profil şəkli")
    history = models.DateTimeField(auto_now_add=True)


# homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

# HOME222222222222222222222222222222222222222222222222222222222222222222
class Slickbox(models.Model):
    image=models.FileField(verbose_name="Şəkil")
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    description=RichTextField(max_length=500,verbose_name="Açıqlama")




# HOME222222222222222222222222222222222222222222222222222222222222222222
    

class Consultant(models.Model):
    name=models.CharField(max_length=100,verbose_name="Adı")
    last_name=models.CharField(max_length=100,verbose_name="Soyadı")
    photo=models.FileField()
    description=RichTextField(max_length=1000,verbose_name="Haqqında")
    email=models.EmailField(max_length=100,verbose_name="E-mail",blank=True)
    phone=models.CharField(max_length=100,verbose_name="Telefon",blank=True)
    occupation=models.CharField(max_length=100,verbose_name="Vəzifə")
    twitter=models.CharField(max_length=100,verbose_name="Twitter")
    facebook=models.CharField(max_length=100,verbose_name="Facebook")
    youtube=models.CharField(max_length=100,verbose_name="Youtube")
    instagram=models.CharField(max_length=100,verbose_name="Instagram")
   