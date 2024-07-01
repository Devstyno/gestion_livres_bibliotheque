from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=255, blank=False, null=False)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.libelle

class Livre(models.Model):
    isbn = models.CharField(max_length=255, unique=True)
    titre = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    editeur = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING, related_name="livres")

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.titre