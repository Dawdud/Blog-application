# -*- coding: utf-8 -*-
from .models import  Projects, Post

def projectlist(request):
    projects= Projects.objects.all().order_by('startproject').reverse()[0]
    return {'projectslist': projects}
def random_post(request):
    random_post= Post.objects.all().order_by('?')[:6]
    return {'random_post': random_post}
def new_post(request):
   new_post= Post.objects.all().order_by('created_date').reverse()[:4]
   return {'new_post': new_post}
def new_conception(request):
    conception= Projects.objects.filter(status=u'zakończono').order_by('startproject')[:5]
    return{'conception': conception}