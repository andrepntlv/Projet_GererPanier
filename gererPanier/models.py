from django.db import models


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(decimal_places=2,max_digits=12)
    stock = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    est_actif = models.IntegerField()

    def __str__(self):
        return self.nom


# class Commande(models.Model):
#     id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     prix = models.DecimalField(decimal_places=2,max_digits=2)
#     etat = models.CharField(max_length=150)
#     type_facturation = models.CharField(max_length=100)
#     est_actif = models.IntegerField()
#
# class CommandeProduit(models.Model):
#     id_produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
#     nombre_produit = models.IntegerField()