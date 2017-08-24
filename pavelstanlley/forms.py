# -*- coding: utf-8 -*-
from django import forms
from .models import Post, Contact, Projects





class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields= ('title','slug', 'text', 'pub_date')
        widgets = {
            'slug': forms.TextInput(attrs={'placeholder': u'Krótka zawartość nagłówka...',}),
        }







class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        email= forms.CharField(required=True)
        widgets = {
            'content': forms.Textarea(attrs={'rows':25, 'cols':80, 'placeholder': u'Wpisz zawartość wiadomości...'}),
            'imie': forms.TextInput(attrs={'size':25}),
            'email': forms.TextInput(attrs={'size':25}),
            'temat': forms.TextInput(attrs={'size':25}),


        }
        fields = ('imie', 'email', 'temat', 'content')

class ProjectsForm(forms.ModelForm):
    class Meta:
        model= Projects
        startproject= forms.DateTimeField(required=True)
        endproject= forms.DateTimeField(required=True)
        otherauthors= forms.CharField(required=False)
        status= forms.DateTimeField(required=True)
        widgets= {

            'descriptionproject':forms.Textarea(attrs={'rows':25, 'cols':60})
        }
        fields= ('projectname',  'startproject','status', 'endproject','otherauthors','descriptionproject')



