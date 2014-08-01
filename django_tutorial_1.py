# tutorial Site Zero
# Django = framework

# il faut noter que nous avons séparé notre fichier en 3 fichiers Python (models.py, views.py, urls.py)
# et un gabarit html (derniers_livres.html)

# models.py

from django.db import models

class Livre(models.Model):
  nom = models.CharField(maxlength=50)
  date_publication = models.DateField()

# views.py

from django.shortcuts import render_to_response
from models import Livre

def derniers_livres(request):
  liste_livres = Livre.objects.order_by('-date_publication')[:10]
  return render_to_response('derniers_livres.html', {'liste_livres': liste_livres})

# urls.py (la configuration de l'URL)

from django.conf.urls.defaults import *

urlpatterns = patterns('',(r'derniers/$', app.views.derniers_livres),)

# html
<!--derniers_livres.html (le gabarit)-->
<ul>
  {% for livre in liste_livres %}
    <li>{{ livre.nom }}</li>
  {% endfor %}
</ul>
