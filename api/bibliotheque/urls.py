from rest_framework import routers

from bibliotheque.views import CategorieViewSet, CategorieAdminViewSet, LivreViewSet, LivreAdminViewSet

router = routers.DefaultRouter()
router.register('categorie', CategorieViewSet, basename='categorie')
router.register('livre', LivreViewSet, basename='livre')
router.register('admin/categorie', CategorieAdminViewSet, basename='admin-categorie')
router.register('admin/livre', LivreAdminViewSet, basename='admin-livre')