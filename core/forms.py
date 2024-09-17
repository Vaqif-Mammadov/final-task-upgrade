from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile,Social,Comment,Reply,User_contact,NewsletterMessage

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    password_repeat = forms.CharField(widget=forms.PasswordInput, label='Repeat Password')

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')

        if password and password_repeat and password != password_repeat:
            raise ValidationError('Passwords do not match')
        

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label='Email Address', max_length=254)
    

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class SocialForm(forms.ModelForm):
    class Meta:
        model = Social
        fields = ['image','name','link','active']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['email', 'url', 'comment']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['reply_text']

class User_contactForm(forms.ModelForm):
    class Meta:
        model = User_contact
        fields = ['name','phone','note','yourconsent']

class FAQForm(forms.Form):
    full_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your message...', 'rows': 7}))


class NewsletterMessageForm(forms.ModelForm):
    class Meta:
        model = NewsletterMessage
        fields = ['user', 'mail1', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
