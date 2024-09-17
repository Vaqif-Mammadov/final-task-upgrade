from django.db import models
from django.contrib.auth.models import User
import random,json
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
    image_icon=models.FileField(verbose_name="Şəkil ikon formasında", default='')
    category = models.CharField(max_length=100,verbose_name="Kateqoriya")
    category2 = models.CharField(max_length=100,verbose_name="İkinci Kateqoriya", default='',blank=True)
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    content = RichTextField(max_length=3000,verbose_name="Məzmun", default='')
    name_lastname = models.CharField(max_length=100,verbose_name="Ad və soyad")
    icon = models.FileField(verbose_name="Profil şəkli")
    history = models.DateTimeField(auto_now_add=True)
    topimg= models.FileField(verbose_name="Üst şəkil",blank=True, default='')
    midimg= models.FileField(verbose_name="Orta şəkil", blank=True, default='')
    botimg= models.FileField(verbose_name="Alt şəkil",blank=True, default='')
    


# homeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

# HOME222222222222222222222222222222222222222222222222222222222222222222
class Slickbox(models.Model):
    image=models.FileField(verbose_name="Şəkil")
    title = models.CharField(max_length=100,verbose_name="Başlıq")
    description=RichTextField(max_length=500,verbose_name="Açıqlama")


class Plan(models.Model):
    name = models.CharField(max_length=100,verbose_name="Adı")
    price_monthly = models.CharField(max_length=100,verbose_name="Aylıq qiymət",default='')
    price_yearly = models.CharField(max_length=100,verbose_name="İllik qiymət",default='')
    description=RichTextField(max_length=500,verbose_name="Açıqlama")
    my_list = models.CharField(max_length=255, default='[]')

    def get_my_list(self):
        return json.loads(self.my_list)

    def set_my_list(self, value):
        self.my_list = json.dumps(value)


class Social(models.Model):
    image = models.FileField(verbose_name="Şəkil")
    name = models.CharField(max_length=100, blank=True, verbose_name="Adı")
    link = models.CharField(max_length=300, blank=True, verbose_name="Linki")
    active = models.BooleanField(default=True, verbose_name="Aktivdir?")

    def get_icon_class(self):
        icon_map = {
            'twitter': 'fa-brands fa-x-twitter',
            'facebook': 'fa-brands fa-facebook-f',
            'google plus': 'fa-brands fa-google-plus-g',
            'instagram': 'fa-brands fa-instagram',
            'pinterest': 'fa-brands fa-pinterest',
            'linkedin': 'fa-brands fa-linkedin',
            
        }
        return icon_map.get(self.name.lower(), 'fa-brands fa-question-circle')



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

    def __str__(self):
        return f"{self.name} {self.last_name}"
   



#    SERVICEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
class Sponsor(models.Model):
    logo=models.FileField(verbose_name="Sponsor loqosu")

#    SERVICEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE


# CONTACTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
class Contact(models.Model):
    icon=models.FileField(verbose_name="Şəkil")
    name = models.CharField(max_length=100,verbose_name="Başlıq", default='[]')
    tel1 = models.CharField(max_length=100,verbose_name="Telefon1", blank=True, default='[]')
    tel2 = models.CharField(max_length=100,verbose_name="Telefon2", blank=True, default='[]')
    mail1 = models.EmailField(verbose_name="E-mail1", blank=True, default='[]')
    mail2 = models.EmailField(verbose_name="E-mail2", blank=True, default='[]')
    adress1 = models.CharField(max_length=200,verbose_name="Ünvan1", blank=True, default='[]')
    adress2 = models.CharField(max_length=200,verbose_name="Ünvan2", blank=True, default='[]')

# CONTACTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT

# PRICINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
class User_contact(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name="Ad")
    phone = models.CharField(max_length=100,verbose_name="Telefon")
    note=RichTextField(max_length=1000,verbose_name="Qeyd")  
    yourconsent=models.BooleanField(default=False)


class FAQQuestion(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    normalized_message = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.message[:50]
    
class Answer(models.Model):
    question = models.ForeignKey(FAQQuestion, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text[:50]    

# PRICINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG


# BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
class NewsletterMessage(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,default='1')
    mail1 = models.EmailField(default='')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    ishappy=models.BooleanField(default=False)

    def _str_(self):
        return self.subject




# BLOGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG


# SINGLE_POST11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111





# SINGLE_POST11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
# class Article(models.Model):
#     category = models.CharField(max_length=100,verbose_name="Kateqoriya")
#     title=models.CharField(max_length=150,verbose_name="Başlıq")
#     author=models.ForeignKey('Consultant', on_delete=models.CASCADE,verbose_name="Yazar")
#     profile = models.ForeignKey('Profile', on_delete=models.CASCADE, verbose_name="Profil", null=True, blank=True)
#     created_date=models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
#     content=RichTextField(verbose_name="Məzmun")
#     mainimage=models.FileField(null=True,blank=True,verbose_name="Əsas şəkil")
#     topimage=models.FileField(null=True,blank=True,verbose_name="Üst şəkil")
#     midimage1=models.FileField(null=True,blank=True,verbose_name="Orta şəkil1")
#     midimage2=models.FileField(null=True,blank=True,verbose_name="Orta şəkil2")
#     midimage3=models.FileField(null=True,blank=True,verbose_name="Orta şəkil3")
#     botimage=models.FileField(null=True,blank=True,verbose_name="Son şəkil")
#     def __str__(self):
#         return self.title
    
class Comment(models.Model):
    email = models.EmailField()
    url = models.URLField(blank=True)
    comment = models.TextField(default="Anonymous")
    created_at = models.DateTimeField(auto_now_add=True)
    profile_id=models.ForeignKey('Profile', on_delete=models.CASCADE)
    new=models.ForeignKey('New', on_delete=models.CASCADE,default='6')
    def __str__(self):
        return f"Comment by {self.author} on {self.created_at}"
    
class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reply_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reply yazan user

    def __str__(self):
        return f"Reply by {self.profile.username} on {self.created_at}"


# SINGLE_POST22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222



# SINGLE_POST22222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222