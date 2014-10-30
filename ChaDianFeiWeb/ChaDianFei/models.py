#!/home/talen/python2.7/bin/python
#coding=UTF8


from django.db import models
from django.contrib import admin

from django import forms
from django.forms import ModelForm

# Create your models here.
class ChaDianFei(models.Model):
    dorm = models.CharField(max_length = 10)
    mail = models.CharField(max_length = 50)
    

admin.site.register(ChaDianFei)


class Subscibe(forms.Form):
    dorm = forms.CharField(max_length=10 ,label='*宿舍号:  ')
    mail = forms.EmailField(label='*电子邮箱:')
    
    

class ContactForm(ModelForm):
    class Meta:
        model = ChaDianFei
        fields = ('dorm', 'mail')
