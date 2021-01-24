from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .decorators import allowed_users
from .models import Produit
from cart.cart import Cart


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

# Source à partir de la ligne d'en dessous : https://pypi.org/project/django-shopping-cart/
# Aide de Kevin Bonga pour la view panier
reduction = 0
prixNet = 0
@login_required(login_url="/login/")
@allowed_users(allowed_groups=['client'])
def panier(request):
    panier = Cart(request).cart.values()
    prixTotal = []
    for prod in panier:
        listQuantite = int(prod.get("quantity"))
        listPrix = prod.get("price")

        if type(listQuantite) == int:
            totalLigne = float(listPrix) * listQuantite
            prixTotal.append(totalLigne)
        else:
            raise TypeError('La quantité doit être en int, les prix en float.')

    prixTotal = sum(prixTotal)

    if prixTotal < 0:
        raise TypeError('Le montant doit être positif.')
    else:
        global reduction
        global prixNet
        if (prixTotal >= 1000):
            prixNet = prixTotal * 80 / 100
            reduction = prixTotal * 20 / 100
        elif (prixTotal >= 500 and prixTotal < 1000):
            prixNet = prixTotal * 90 / 100
            reduction = prixTotal * 10 / 100
        elif (prixTotal >= 250 and prixTotal < 500):
            prixNet = prixTotal * 95 / 100
            reduction = prixTotal * 5 / 100
        else:
            reduction = 0

    context = {
        'prixTotal': prixTotal,
        'reduction': reduction,
        'prixNet' : prixNet
    }
    return render(request, 'produit/panier.html', context)

@login_required(login_url="/accounts/login/")
@allowed_users(allowed_groups=['client'])
def ajout_article(request, id):
    cart = Cart(request)
    product = Produit.objects.get(id=id)
    cart.add(product=product)
    return redirect("panier")

@login_required(login_url="/accounts/login/")
@allowed_users(allowed_groups=['client'])
def suppression_article(request, id):
    cart = Cart(request)
    produit = Produit.objects.get(id=id)
    cart.remove(produit)
    return redirect("panier")

# quantite = 0
@login_required(login_url="/accounts/login/")
@allowed_users(allowed_groups=['client'])
def item_increment(request, id):
    # global quantite
    # global message
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

@login_required(login_url="/accounts/login/")
@allowed_users(allowed_groups=['client'])
def item_decrement(request, id):
    cart = Cart(request)
    produit = Produit.objects.get(id=id)
    cart.decrement(product=produit)
    return redirect("panier")

@login_required(login_url="/accounts/login/")
@allowed_users(allowed_groups=['client'])
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("panier")