from django.shortcuts import render
from .models import Produit

def gererproduit(request):
    produits = Produit.objects.all().filter(est_actif=1)
    context = {
        'produits' : produits,
    }
    return render(request, 'produit/produit.html', context)