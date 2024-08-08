from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=150,verbose_name="Başlıq")
    content=RichTextField(verbose_name="Məzmun")
    created_date=models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    image=models.FileField(null=True,blank=True,verbose_name="Şəkil")
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Məqalə")
    comment_author=models.CharField(max_length=150, verbose_name="Müəllif")
    comment_content=RichTextField(verbose_name="Məzmun")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Yaradılma tarixi")
    def __str__(self):
        return self.comment_author