from django.contrib import admin
from bibliotheque.models import Categorie, Livre

# Register your models here.
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle', 'date_created', 'date_updated', 'active')

class LivreAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'titre', 'categorie', 'auteur', 'editeur', 'date_created', 'date_updated', 'active')

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Livre, LivreAdmin)