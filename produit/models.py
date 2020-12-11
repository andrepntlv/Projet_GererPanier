from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(decimal_places=2,max_digits=2)
    stock = models.IntegerField()
    image = models.ImageField()
    est_actif = models.IntegerField()

class Client(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    date_de_naissance = models.DateField()
    email = models.EmailField(max_length=30)
    telephone = models.CharField(max_length=15)
    pseudo = models.CharField(max_length=15)
    password = models.CharField(max_length=40)
    est_actif = models.IntegerField()

class Commande(models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    prix = models.DecimalField(decimal_places=2,max_digits=2)
    etat = models.CharField(max_length=150)
    type_facturation = models.CharField(max_length=100)
    est_actif = models.IntegerField()

class CommandeProduit(models.Model):
    id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    nombre_produit = models.IntegerField()