# Étapes de base pour démarrer un projet Django avec DRF

1. **Installer Django et Django REST Framework**

Assurez-vous d'avoir Python installé, puis créez un environnement virtuel. Ensuite, installez Django et Django REST Framework via pip :

    ```bash
        pip install django djangorestframework
    ```

2. **Créer un projet Django**

Utilisez la commande Django pour créer un nouveau projet :

    ```bash
        django-admin startproject nom_du_projet
    ```

Remplacez `nom_du_projet` par le nom que vous souhaitez donner à votre projet.

3. **Configurer la base de données**

Allez dans le répertoire du projet et configurez la base de données dans le fichier `settings.py`.

4. **Créer une application Django**

Utilisez la commande Django pour créer une nouvelle application à l'intérieur de votre projet :

   ```bash
       python manage.py startapp nom_de_l_application
   ```

Remplacez `nom_de_l_application` par le nom de votre application.

5. **Configurer DRF dans votre application**

    - Ajoutez `'rest_framework'` aux `INSTALLED_APPS` dans `settings.py`.
    - Configurez les paramètres de DRF selon vos besoins (par exemple, `DEFAULT_AUTHENTICATION_CLASSES`, `DEFAULT_PERMISSION_CLASSES`).

6. **Créer des modèles**

Définissez vos modèles dans le fichier `models.py` de votre application.

7. **Créer des serializers**

Créez des serializers dans `serializers.py` pour transformer vos modèles en JSON et vice versa.

8. **Configurer les vues**

Créez des vues basées sur les classes ou des vues fonctionnelles dans `views.py`. Utilisez les mixins et les classes génériques de DRF pour simplifier la création de vues RESTful.

9. **Configurer les routes (URLs)**

Ajoutez des routes (URLs) dans `urls.py` de votre application pour associer les vues aux endpoints API.

10. **Effectuer les migrations**

Initialisez la base de données avec les tables nécessaires en exécutant les migrations :

    ```bash
        python manage.py makemigrations
        python manage.py migrate
    ```

11. **Lancer le serveur de développement**

Démarrez le serveur de développement Django pour tester votre projet :

    ```bash
        python manage.py runserver
    ```

12. **Tester les endpoints API**

    Utilisez un outil comme Postman ou curl pour tester les endpoints que vous avez créés.
