# Gestion des Livres d'une Bibliothèque

On souhaite mettre en place une API permettant de gérer livres d’une
bibliothèque. Les livres sont regroupés par catégories. Chaque livre
dispose d’un code ISBN unique, d’un titre, de la date de publication, le
nom de l’auteur, le nom de l’éditeur. La catégorie est caractérisée par un id
et le libellé de la catégorie. (Exemple de catégorie : Fixion, Policier, Conte,
Harlequin, Science etc....)

## L’API doit permettre de

- Lister tous les livres
- Chercher un livre en particulier par son id
- Lister la liste des livres d’une catégorie
- Lister une catégorie
- Chercher une catégorie par son id
- Lister toutes les catégories
- Supprimer un livre
- Supprimer une categorie
- Modifier les informations d’un livre
- Modifier le libellé d’une categorie

## Taches

1. Vous devez construire votre API à l’aide de Django REST Framework / base de
données SQLite
2. Vous devez documenter votre API en précisant les réponses que vous
obtenez après avoir exécuter chaque endpoint
3. Déployer votre API sur la plateforme Cloud Heroku
Pour vous aider, on vous donne le Modèle Relationnel suivant :
    `

        CATÉGORIES(id, libelle_catégorie)
        LIVRES(id, isbn, titre, date_publication, auteur, éditeur, #catégorie_id)

    `
