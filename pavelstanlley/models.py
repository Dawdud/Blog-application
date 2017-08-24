# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
# Create your models here.
class Post(models.Model):

    title= models.CharField(max_length=100)
    slug= models.SlugField(unique= True,)
    text= models.TextField()
    category= models.CharField(max_length=100)
    author= models.ForeignKey('auth.User')
    created_date= models.DateTimeField(default= timezone.now)
    pub_date= models.DateTimeField()
    edit_pub_date= models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pub_date= timezone.now()
        self.edit_pub_date= timezone.now()
        self.save()
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})
class content(models.Model):
    post= models.ForeignKey(Post, related_name='Post')
    text= models.TextField()
class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    views= models.IntegerField(default=0)
    slug=models.SlugField()
    def save(self, *args, **kwargs):
        self.slug= slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name

class Contact(models.Model):
    imie= models.CharField(max_length=120,)
    email= models.EmailField()
    temat= models.CharField(max_length=50)
    content= models.TextField()
    created_date= models.DateTimeField(default= timezone.now)
    def   publish(self):
        self.save()
    def __unicode__(self):
        return self.subject

class Projects(models.Model):
    CONCEPTION='koncepcja'
    IN_PROGRESS= u'w trakcie realizacji'
    BREAK=u'przerwano'
    END=u'zakończono'
    STATUS_CHOICES= (
        (CONCEPTION, u'pomysł projektu'),
        (IN_PROGRESS, u'W trakcie realizacji'),
        (BREAK, u'Projekt przerwano'),
        (END, u'Projekt zakończono'),
    )
    slug= models.SlugField(unique= True)
    projectname= models.CharField(max_length=120)
    startproject= models.DateTimeField()
    endproject= models.DateTimeField()
    status= models.CharField(choices=STATUS_CHOICES, default=CONCEPTION, max_length=50)
    author= models.CharField(max_length=50)
    otherauthors= models.CharField(max_length=120, blank= True, null= True)
    descriptionproject= models.TextField()



