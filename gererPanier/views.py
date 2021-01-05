from django.shortcuts import render, redirect
from .models import Produit
from cart.cart import Cart
from django.contrib import messages

def gererproduit(request):
    produits = Produit.objects.all().filter(stock__gt=0).filter(est_actif=1)
    context = {
        'produits' : produits,
    }
    return render(request, 'produit/produits.html', context)

def detailProduit(request, id):
    produit = Produit.objects.get(pk=id)
    context = {
        'produit' : produit,
    }
    return render(request, 'produit/detailProduit.html', context)

# Source à partir de la ligne d'en dessous: https://pypi.org/project/django-shopping-cart/
# Aide de Kevin Bonga
def panier(request):
    panier = Cart(request).cart.values()
    prixTotal = []
    for prod in panier:
        listProdQuantite = int(prod.get("quantity"))
        listProdPrix = prod.get("price")

        totalLig = float(listProdPrix) * listProdQuantite
        prixTotal.append(totalLig)

    prixTotal = sum(prixTotal)
    context = {
        'prixTotal': prixTotal,
    }
    return render(request, 'produit/panier.html', context)

def ajout_article(request, id):
    cart = Cart(request)
    product = Produit.objects.get(id=id)
    cart.add(product=product)
    return redirect("panier")

def suppression_article(request, id):
    cart = Cart(request)
    produit = Produit.objects.get(id=id)
    cart.remove(produit)
    return redirect("panier")

# quantite = 0
def item_increment(request, id):
    # global quantite
    cart = Cart(request)
    produit = Produit.objects.get(id=id)
    # panier = Cart(request).cart.values()
    # panier[id]
    # for prod in panier:
    #     if prod.get('id')==id:
    #         quantite = int(prod.get("quantity"))
    # if (produit>produit.stock):
    #      messages.error(request,'Il n\'y a pas assez de quantité en stock.')
    # else:
    cart.add(product=produit)
    return redirect("panier")

def item_decrement(request, id):
    cart = Cart(request)
    produit = Produit.objects.get(id=id)
    cart.decrement(product=produit)
    return redirect("panier")

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("panier")