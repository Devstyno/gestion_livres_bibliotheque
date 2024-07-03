# Étapes de base pour démarrer un projet Django avec DRF

1. **Installer Django et Django REST Framework**

    S'assurez d'avoir Python installé, puis créer un environnement virtuel. Ensuite, installer Django et Django REST Framework via pip :

    ```bash
        pip install django djangorestframework
    ```

2. **Créer un projet Django**

    Utiliser la commande Django pour créer un nouveau projet :

    ```bash
        django-admin startproject nom_du_projet
    ```

    Remplacer `nom_du_projet` par le nom qu'on souhaite donner à notre projet.

3. **Configurer la base de données**

    Aller dans le répertoire du projet et configurer la base de données dans le fichier `settings.py`.

4. **Créer une application Django**

    Utiliser la commande Django pour créer une nouvelle application à l'intérieur de notre projet :

   ```bash
        python manage.py startapp nom_de_l_application
   ```

    Remplacer `nom_de_l_application` par le nom de notre application.

5. **Configurer DRF dans votre application**

    - Ajouter `'rest_framework'` aux `INSTALLED_APPS` dans `settings.py`.
    - Configurer les paramètres de DRF selon nos besoins (par exemple, `DEFAULT_AUTHENTICATION_CLASSES`, `DEFAULT_PERMISSION_CLASSES`).

6. **Créer des modèles**

    Définir nos modèles dans le fichier `models.py` de notre application.

7. **Créer des serializers**

    Créer des serializers dans `serializers.py` pour transformer nos modèles en JSON et vice versa.

8. **Configurer les vues**

    Créer des vues basées sur les classes ou des vues fonctionnelles dans `views.py`. Utiliser les mixins et les classes génériques de DRF pour simplifier la création de vues RESTful.

9. **Configurer les routes (URLs)**

    Ajouter des routes (URLs) dans `urls.py` de notre application pour associer les vues aux endpoints API.

10. **Effectuer les migrations**

    Initialiser la base de données avec les tables nécessaires en exécutant les migrations :

    ```bash
        python manage.py makemigrations
        python manage.py migrate
    ```

11. **Lancer le serveur de développement**

    Démarrer le serveur de développement Django pour tester notre projet :

    ```bash
        python manage.py runserver
    ```

12. **Tester les endpoints API**

    Utiliser un outil comme Postman ou curl pour tester les endpoints que nous avons créés.
