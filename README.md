django
======

web programming, interface for Iterameta

install Django

django-admin.py startproject mvp_landing # start the project
ls # mvp_landing
cd mvp_landing
ls # manage.py mvp_landing

# launch the database
python manage.py syncdb
superuser: yes

# 
python manage.py runserver
# open browser: IP + /admin

# start first django application

# django.contrib.admin powerful app
# urls.py file replacing 'admin' by 'abc' and see result

# creating apllication signups for people to join
python manage.py startapp signups
# signups: __init__.py, admin.py, models.py, tests.py, views.py

# models.py to set up the model and add Django admin capabilities
from django.db import models
from django.utils.encoding import smart_unicode

class SignUp(models.Model):
  first_name = models.CharField(max_length=120, null=True, blank=True)
  last_name = models.CharField(max_length=120, null=True, blank=True)
  email = models.EmailField(null=False,blank=False)
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  updated = models.DateTimeField(auto_now_add=False, auto_now=True)
  
  def __unicode__(self):
    retrn smart_unicode(self.email)

# settings.py
INSTALLED_APPS.. 'signups',

python manage.py syncdb
python manage.py runserver

# admin.py
from django.contrib import admin
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
  class Meta:
    model = SignUp
    
admin.site.register(SignUp, SignUpAdmin)
  
# views for sign up
# settings.py

# template_location
TEMPLATE_DIRS = (
  os.path.join(os.path.dirname(BASE_DIR) 'static', 'templates'),
  )

# signup.html
<!DOCTYPE html>
  <html>
    <head>
    
    </head>
    
    <body>
    
      <h1> Join now </h1>
        <form method = 'POST' action=''>
          <input type='text'>
          
          <input type='submit'>
    </body>
  </html>

# urls.py
urlpatterns = patterns('', url(r'^$', 'signups.view.home', name='home'), ..)

# views.py
from django.shortcuts import render, render_to_response, RequestContext

def home(request):
  return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

# forms.py
from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
  class Meta:
    model = SignUp

# views.py
from .forms import SignUpForm

def home(request):
  form = SignUpForm(request.POST or None)
  
  if form.is_valid():
    save_it = form.save(commit=False)
    save_it.save()
    
  return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

# signup.html
<!DOCTYPE html>
  <html>
    <head>
    
    </head>
    
    <body>
    
      <h1> Join now </h1>
        <form method = 'POST' action=''> {% csrf_token %}
          {{form.as_p}}

          <input type='submit'>
    </body>
  </html> 

# 7/21: serve django static files in local development environment
# settings.py

if DEBUG:
  MEDIA_URL = '/media/'
  STATIC_ROOT = os.path.join(os.path.dirnam(BASE_DIR), 'static', 'static-only')
  MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static', 'media')
  STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), 'static', 'static')
    )
# creating new directories static, media, static, static-only, templates


# urls.py
from django.conf import settings
from django.conf.urls.static import static
..
if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# terminal
python manage.py collectstatic
pthon manage.py runserver

# getbootstrap.com
# 8/21: add twitter bootstrap version 3 framework to Django Project Templates
# jumbotron to copy codesource
# in templates, make base.html, paste

# signup.html
{% extends 'base.html' %}

{% blog content %}
<h1>Join Now</h1>
<form method='POST' action=''> {% crsf_token %}
  {{form.as_p}}
</form>
{% endblock %}

# save css file to static/css.. then
python manage.py collectstatic

# save js to static/js ..

# 9/21: add custom styles & css to twitter bootstrap 3

# 10/21 learn to customize twitter bootstrap 3

# signup.html
{% extends 'base.html' %}

{% blog content %}
<h1>Join Now</h1>
<form method='POST' action=''> {% crsf_token %}
  {{form.as_p}}
  <input type='submit' class='btn btn-success btn-lg'>
</form>
{% endblock %}


# 11/21 django messages and messagin framework
// views.py
from django.contrib import messages

from .forms import SignUpForm

def home(request):
  form = SignUpForm(request.POST or None)
  
  if form.is_valid():
    save_it = form.save(commit=False)
    save_it.save()
    messages.success(request, 'Thank you for joining')
    
  return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

// base.html
<div class='container'>
{% if messages %}
  <div class='row'>
  {% for message in messages %}
  <p{% if message.tags %} class='{{message.tags}}'{%endif %}> {{message}} </p>
  {% endfor % }
  </div>
</div>

// 12/21: Django HTTP redirect and standard pages
// views.py
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages

from .forms import SignUpForm

def home(request):
  form = SignUpForm(request.POST or None)
  
  if form.is_valid():
    save_it = form.save(commit=False)
    save_it.save()
    messages.success(request, 'Thank you for joining')
    return HttpResponseRedirect('/thank-you/', 'signups.views.thankyou', name='thankyou')
  return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

// urls.py
url(r'^thank-you/$',)

// views.py
def thankyou(request):
  return render_to_response('thankyou.html', locals(), context_instance=RequestContext(request))
  
// thankyou.html
{% extends 'base.html' %}

{% block content %}

<h4> Thank you for joining </h4>

{% endblock %}

// 13/21 add & update twitter bootstrap navbar

// 14/21 add basic paypal button to Django project template

// 15/21 django update thank you page and view after paypal purchase

// django emailing send a confirmation email using gmail

// django 1.6 for Webfaction - setup Webfaction accounts to go live















  
