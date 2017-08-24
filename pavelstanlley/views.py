# -*- coding: utf-8 -*-
from datetime import date, datetime
from django.forms import inlineformset_factory, formset_factory
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404,redirect, render_to_response
from django.contrib.auth.decorators import  user_passes_test
from django.template import RequestContext
from .models import Post,Contact, Projects, Category
from django.utils import timezone
from .forms import  ContactForm, PostForm,ProjectsForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def category(request,category_name_slug):
    context_dict={}
    try:
        category= Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Post.objects.filter(category= category)
        context_dict['pages']=  pages
        context_dict['category']= category
    except Category.DoesNotExist:
           pass
    return render(request, 'pavelstanlley/category.html', context_dict)
def index(request):
    post= Post.objects.all().order_by('pub_date').reverse()
    paginator= Paginator(post,4)
    page= request.GET.get('page')
    try:
        posts= paginator.page(page)
    except PageNotAnInteger:
        posts= paginator.page(1)
    except EmptyPage:
        posts= paginator.page(paginator.num_pages)

    return render_to_response('pavelstanlley/index.html', {'post':posts} )

def post_detail(request, slug):
    post= get_object_or_404(Post, slug=slug)
    return render_to_response( 'pavelstanlley/post_detail.html', {'post':post})
def projects_detail(request, slug):

    projects= get_object_or_404(Projects, slug=slug)
    return render_to_response('pavelstanlley/project_detail.html', {'projects': projects} )

def projects(request):
    projects= Projects.objects.all().order_by('startproject').reverse()
    return render_to_response('pavelstanlley/projects.html', {'projects': projects} )

class PostYear(YearArchiveView):
    queryset = Post.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
class PostMonth(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "pub_date"
    allow_future = True
def Legal_inforamtion(request):

    return render_to_response('pavelstanlley/prawne.html',)
def about(request):

    return render_to_response('pavelstanlley/about.html',)
def endproject(request):
    end=Projects.objects.order_by('startproject').filter(status=u'zakończono')
    return render_to_response('pavelstanlley/endproject.html',{'end':end},)
def conceptions(request):
    conceptions=Projects.objects.order_by('startproject').filter(status='koncepcja')
    return render_to_response('pavelstanlley/conceptions.html',{'conceptions':conceptions},)
def break_projects(request):
    break_project=Projects.objects.order_by('startproject').filter(status='Projekt przerwano')
    return render_to_response('pavelstanlley/break_projects.html',{'break_project': break_project},)
def progress_projects(request):
    progress=Projects.objects.order_by('startproject').filter(status='W trakcie realizacji')
    return render_to_response('pavelstanlley/progress_projects.html', {'progress': progress},)
@user_passes_test(lambda u: u.is_superuser)
def restricted(request):
        return render(request, 'pavelstanlley/restricted.html')
@user_passes_test(lambda u: u.is_superuser)
def Messages(request):
  messages= Contact.objects.all().order_by('created_date').reverse()
  return   render(request, 'pavelstanlley/Messages.html', {'messages': messages})
@user_passes_test(lambda u: u.is_superuser)
def messages_detail(request, pk):
    message= get_object_or_404(Contact, pk=pk)
    return render(request,'pavelstanlley/messages_details.html',{'message':message})
@user_passes_test(lambda u: u.is_superuser)
def message_deleting(request,pk=None):
    delete_message= get_object_or_404(Contact, pk=pk)
    delete_message.delete()
    return redirect("Messages")
@user_passes_test(lambda u: u.is_superuser)
def Post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post= form.save(commit= False)
            post.author= User.objects.get(is_superuser=True)
            post.pub_date= timezone.now()
            post.save()
            return redirect('post_detail', slug= post.slug)
    else:
        form= PostForm
    return render(request, 'pavelstanlley/postnew.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def postedit(request, pk):
    post= get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form= PostForm(request.POST, request.FILES)
        if form.is_valid() :
            post= form.save(commit= False)
            post.author= User.objects.get(is_superuser=True)
            post.edit_pub_date= timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
         form= PostForm(instance=post)
    return render(request, 'pavelstanlley/postedit.html', {'form': form}, )
def contact(request):
    form_contact= ContactForm
    random_post= Post.objects.all().order_by('?')[:6]
    if request.method =='POST':
        form= form_contact(data= request.POST)
        if form.is_valid():
            f= form.save()
            f.save()
            imie= request.POST.get('name_surname','')
            email= request.POST.get('email')
            temat= request.POST.get('subject','')
            content= request.POST.get('content','')
            template= get_template('pavelstanlley/contact_template.txt')
            context= Context({'name_surname':imie,
                              'email':email,
                              'subject':temat,
                              'content':content,
                              })
            content= template.render(context)
            email_to= EmailMessage(
                "Nowa widomosc od uzytkownika",
                content,
                "pavelstanlley" +" ",
                ['dawdud12@gmail.com'],
                headers= {'reply_to':email,}
            )
            email_to.send()
            return HttpResponse("Dzieki za kontkat")

    return render_to_response ( 'pavelstanlley/contact.html', {'form':form_contact, 'random_post': random_post},)

def projectsnew(request):
    if request.method=="POST":
        form= ProjectsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
           f= form.save()
           f.save()
           return HttpResponse("Dodano nowy projekt")
    else:
        form= ProjectsForm
    return render_to_response('pavelstanlley/projectsnew.html', {'form': form}, )


