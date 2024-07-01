from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from bibliotheque.models import Categorie, Livre
from bibliotheque.serializers import CategorieListSerializer, CategorieDetailSerializer, LivreListSerializer, LivreDetailSerializer
from bibliotheque.permissions import IsAdminUser

from interfaces.module import MultipleSerializerMixin

class CategorieViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CategorieListSerializer
    detail_serializer_class = CategorieDetailSerializer

    # Read
    def get_queryset(self):
        return Categorie.objects.filter(active=True)

class LivreViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = LivreListSerializer
    detail_serializer_class = LivreDetailSerializer

    # Read
    def get_queryset(self):
        return Livre.objects.all()

class CategorieAdminViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CategorieListSerializer
    detail_serializer_class = CategorieDetailSerializer
    permission_classes = [IsAdminUser]

    # Read
    def get_queryset(self):
        return Categorie.objects.all()

class LivreAdminViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = LivreListSerializer
    detail_serializer_class = LivreDetailSerializer
    permission_classes = [IsAdminUser]

    # Read
    def get_queryset(self):
        return Livre.objects.all()