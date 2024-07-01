from rest_framework.serializers import ModelSerializer, SerializerMethodField

from bibliotheque.models import Categorie, Livre

class LivreListSerializer(ModelSerializer):

    class Meta:
        model = Livre
        fields = ('id', 'isbn', 'titre', 'auteur', 'editeur')

class LivreDetailSerializer(ModelSerializer):

    class Meta:
        model = Livre
        fields = ('id', 'isbn', 'titre', 'categorie', 'auteur', 'editeur', 'date_created', 'date_updated', 'active')

class CategorieListSerializer(ModelSerializer):

    class Meta:
        model = Categorie
        fields = ('id', 'libelle', 'date_created')

class CategorieDetailSerializer(ModelSerializer):
    
    livres = SerializerMethodField()

    class Meta:
        model = Categorie
        fields = ('id', 'libelle', 'livres', 'date_created', 'date_updated', 'active')
    
    def get_livres(self, instance):
        queryset = instance.livres.all()
        serializer = LivreListSerializer(queryset, many=True)
        return serializer.data