from django import forms
from website.models import Contact, NewsLetter
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
  

class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = '__all__'