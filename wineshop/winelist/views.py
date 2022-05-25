from django.views.generic import ListView
from . import models

class WineListView(ListView):
	model = models.Wine
