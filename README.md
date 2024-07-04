
# Application de Gestion de Réservations de Voyages

## Introduction

Cette application est conçue pour gérer les réservations de voyages en intégrant des mesures de sécurité pour protéger contre les vulnérabilités courantes identifiées par l'OWASP. L'application peut fonctionner en deux modes :
- **Mode Safe** : Les mesures de sécurité sont activées pour protéger contre les attaques courantes.
- **Mode Unsafe** : L'application est volontairement vulnérable aux attaques courantes.

## Fonctionnalités

1. **Enregistrement de compte utilisateur** : Créer un compte avec un nom d'utilisateur et un mot de passe.
2. **Connexion utilisateur** : Se connecter avec les identifiants créés.
3. **Recherche de voyages** : Rechercher des voyages disponibles avec les détails correspondants.
4. **Réservation de voyages** : Réserver des voyages disponibles et gérer les réservations.
5. **Confirmation de réservation** : Valider les réservations et envoyer une confirmation par email.

## Sécurités Intégrées

### Injection SQL

- **Description** : L'injection SQL permet à un attaquant d'exécuter des requêtes SQL arbitraires sur la base de données.
- **Prévention** : Utiliser des requêtes paramétrées et ORM (Object Relational Mapping) comme SQLAlchemy.

### XSS (Cross-Site Scripting)

- **Description** : L'attaquant injecte du code malveillant dans les pages web vues par d'autres utilisateurs.
- **Prévention** : Échapper et valider toutes les entrées utilisateur avant de les afficher.

### CSRF (Cross-Site Request Forgery)

- **Description** : L'attaquant incite un utilisateur authentifié à exécuter des actions non souhaitées sur une application où il est authentifié.
- **Prévention** : Utiliser des jetons CSRF pour valider les requêtes.

### Force Brute

- **Description** : L'attaquant essaie un grand nombre de combinaisons de mots de passe pour accéder à un compte.
- **Prévention** : Implémenter un verrouillage de compte après plusieurs tentatives échouées.

### Hachage de Mots de Passe

- **Description** : Stocker les mots de passe en clair dans la base de données est une mauvaise pratique.
- **Prévention** : Utiliser des algorithmes de hachage sécurisés pour stocker les mots de passe.

## Instructions pour Exécuter l'Application

### Prérequis

- Python 3.x
- Node.js
- npm (Node Package Manager)

### Installation

1. Clonez le dépôt de l'application :
    ```sh
    git clone https://github.com/ChemaaOmar/AppVoyage
    cd AppVoyage
    ```

2. Installez les dépendances backend :
    ```sh
    cd backend
    python -m venv venv
    source venv/bin/activate  # Sur Windows : venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Installez les dépendances frontend :
    ```sh
    cd ../frontend
    npm install
    ```

### Configuration

1. Créez un fichier `.env` dans le répertoire `backend` et ajoutez les configurations nécessaires :
    ```
    FLASK_APP=app.py
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite3
    ```

2. Initialisez la base de données :
    ```sh
    cd backend
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

### Exécution

1. Lancez le serveur backend :
    ```sh
    cd backend
    flask run
    ```

2. Lancez le serveur frontend :
    ```sh
    cd frontend
    npm start
    ```

### Utilisation

1. Ouvrez votre navigateur et accédez à `http://localhost:3000`.
2. Enregistrez un compte et connectez-vous pour utiliser l'application.
3. Testez les fonctionnalités de recherche et de réservation de voyages.

## Basculement entre Mode Safe et Mode Unsafe

- Le mode peut être basculé en utilisant un bouton dédié dans l'interface utilisateur. Lors du basculement, l'application rechargera automatiquement pour appliquer les changements.

## Conclusion

Cette application intègre des mesures de sécurité pour protéger contre les attaques courantes et illustre l'importance de la sécurité dans le développement d'applications web.
