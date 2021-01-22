from django.db import models

# https://tutorial.djangogirls.org/fr/ aide pour mon model
class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(decimal_places=2,max_digits=12)
    stock = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    est_actif = models.IntegerField()

    def __str__(self):
        return self.nom
