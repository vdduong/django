# 
python manage.py startapp sondages # créer notre première application

# le fonctionnement est strictement le même que la commande
startproject

# models.py
class Sondage(models.Model):
  pass

class Reponse(models.Model):
  pass


# champs et fonctions
# notre modèle 'sondage' doit contenir les champs 'question' et 'date de publicaiton'
# quant au modèle 'Reponse': 'sondage', 'choix', 'nombre de votes'
# en Django ça donne:
class Sondage(models.Model):
  question = models.CharField(max_length=200)
  date_publication = models.DateTimeField()

class Repose(models.Model):
  sondage = models.ForeignKey(Sondage) # une relation avec un modèle
  choix = models.CharField(max_length=200)
  nb_votes = models.IntegerField()

# ajouter l'application au projet
# pour joindre l'application au projet, faut modifier le fichier de configuration settings.py
INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sites',
  'django.contrib.messages',
  'tuto_sdz.sondages',
  # uncomment the next line to enable the admin:
  # 'django.contrib.admin'
  )

# tuto_sdz et sondages dans le code présent correspondent respectivement au nom du projet 
# et au nom de l'application

# afficher la structure SQL de mes modèles
# permettre de vérifier si l'application 'sondages' a bien été prise en compte
python manage.py sql sondages
BEGIN;
CREATE TABLE 'sondages_sondage' (
  'id' integer NOT NULL PRIMARY KEY,
  'question' varchar(200) NOT NULL,
  'date_publication' datetime NOT NULL
  )
;
CREATE TABLE 'sondages_reponse' (
  'id' integer NOT NULL PRIMARY KEY,
  'sondage_id' integer NOT NULL REFERENCES 'sondages_sondage' ('id'),
  'choix' varchar(200) NOT NULL,
  'nb_votes' integer NOT NULL
  )
;
COMMIT;


# générer la base de données
# on va utiliser le fichier  manage.py
python manage.py syncdb

Creating table auth_permission
Creating table auth_group_permissions
Creating table auth_group
Creating table auth_user_user_permissions
Creating table auth_user_groups
Creating table auth_user
Creating table auth_message
Creating table django_content_type
Creating table django_session
Creating table django_site
Creating table sondages_sondage
Creating table sondages_reponse

# You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (Leave blank to use 'camille'): Cam
E-mail address: cam@siteduzero.com
Password: 
Password (again): 
Superuser created successfully.
Installing index for auth.Permission model
Installing index for auth.Group_permissions model
Installing index for auth.User_user_permissions model
Installing index for auth.User_groups model
Installing index for auth.Message model
Installing index for sondages.Reponse model
No fixtures found.

# réalisation des views
# views.py

#-*- codiing: utf-8 -*-
def homepage(request):
  return True

# la fonction doit toujours avoir comme argument premier 'request', c'est obligatoire
# et elle doit toujours retourner qq chose
# module = nom du module (sondages, pour nous)
# model = définition d'un modèle (Sondage)
# model1 = définition d'un modèle (Réposnes)

# from module.models import model, model1
from sondages.models import Sondage, Reponse

# nous voulons récupérer tous les sondages. nous devons donc faire une requête Django
def homepage(request):
  list_sondages = Sondage.objects.all()
  return True

from django.shortcuts import render_to_response
# voici les différents paramètres dont nous allons nous servir
render_to_response(template_name, list_variables)

def homepage(request):
  list_sondages = Sondage.objects.all()
  return render_to_responses('sondages/homepage.html',{'list_sondages':list_sondage})
# django/tuto_sdz/templates/sondages/homepage.html
def homepage(request):
  list_sondages = Sondage.objects.all()
  return render_to_responses('sondages/homepage.html', {'list_sondages': list_sondages, \
    'page_title': 'Accueil des sondages'})

# le gestionnaire d'URLs
# urls.py
from django.conf.urls.defaults import *
# uncomment the next two lines to enable the admin
# from django.contrib import admin
# admin.autodiscover()

# une vue est reliée à une ou plusieurs URLs
urlpatterns = patterns('',
  # examples:
  # (r'^tuto_sdz/', include('tuto_sdz.foo.urls')),
  
  # uncomment the admin/doc line below to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
  
  # uncomment the next line to enable the admin:
  # (r'^admin/', include(admin.site.urls)),
  )

# urlpatterns = variable va devoir contenir toutes nos URLs
from django.conf.urls.defaults import *
urlpatterns = patterns('',
  (r'^sondages/$', 'sondages.views.homepage')
  )

# les gabarits
# deux variables sont envoyées à la vue: page_title et list_sondages
# créer un dossier sondages dans votre dossier de templates et à l'intérieur, définissez le fichier homepage.html

Bonjour {% if not username %} visiteurs {% else %} {{username}}{% endif %}.

# en plus décortiqué et plus posé
Bonjour

{% if not username %} <!-- Si la variable username n existe pas -->
  visiteur <!-- on affiche visiteur -->
  {% else %} <!-- Sinon, si elle existe, on l affiche -->
    {{ username }}

{% endif %}

















