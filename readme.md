Here's the README.md translated into French:

---

# Système de Gestion des Clients et des Assurances

Il s'agit d'une application web basée sur Flask pour la gestion des clients et des assurances. Elle permet aux utilisateurs d'effectuer des opérations CRUD (Créer, Lire, Mettre à jour, Supprimer) sur les clients et les assurances.

## Fonctionnalités

- Ajouter de nouveaux clients et assurances
- Voir les clients et assurances existants
- Mettre à jour les noms des clients et les polices d'assurance
- Supprimer des clients et assurances

## Prérequis

- Python (3.6 ou version ultérieure)
- Flask
- Flask-SQLAlchemy

## Installation

1. Clonez le dépôt :

    ```bash
    git clone <URL-du-dépôt>
    ```

2. Accédez au répertoire du projet :

    ```bash
    cd gestion-clients-assurances
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Lancez l'application Flask :

    ```bash
    python app.py
    ```

2. Ouvrez votre navigateur web et accédez à [http://localhost:5000/](http://localhost:5000/) pour accéder à l'application.

3. Utilisez les formulaires fournis pour ajouter, afficher, mettre à jour et supprimer des clients et assurances.

## Structure du Projet

```
gestion-clients-assurances/
│
├── app.py              # Fichier principal de l'application Flask
├── bd/                 # Répertoire pour le fichier de base de données SQLite
│   └── database.db     # Fichier de base de données SQLite
├── templates/          # Modèles HTML
│   └── home.html       # Modèle HTML principal
└── README.md           # Ce fichier README
```

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

- Ce projet a été créé dans le cadre d'un exercice d'apprentissage.
- Documentation Flask : [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- Documentation SQLAlchemy : [https://docs.sqlalchemy.org/](https://docs.sqlalchemy.org/)

---

N'hésitez pas à personnaliser davantage le fichier README.md pour inclure toute information supplémentaire ou des instructions spécifiques à votre projet.