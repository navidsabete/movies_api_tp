# TP Flask - Gestion de films avec une API

## Pré-requis et éxécution
1. Installer VS Code, Oracle DB, l'extension 'Oracle SQL Developer pour VS Code'
2. Ouvrir Oracle SQL Developer sur VS Code et ajouter une connection
    - a. **Connection Name** : MiniNetflixDB
    - b. **Auth Type, Role** : Default
    - c. **Username** : system, **Password** : mot de passe choisi lors de l'installation d'Oracle DB
    - d. **Connection Type** : Basic
    - e. **Hostname** : localhost, **Port** : 1521
    - f. **Type** : Service Name, **Service Name** : XEPDB1
    - g. Tester la connection et sauvegarder les informations
3. Se connecter à la **MiniNetflixDB**
4. Éxécuter le script 'sql/create.sql' pour créer les tables
5. Pour faire fonctionner cette application Flask, il est important de :
    - a. s'assurer que Python est bien installé sur la machine
    - b. vérifier que les librairies importées sont bien installées --> command type :"[myLocalPathToPythonExe]/python.exe -m pip install oracledb"
        - oracledb
        - flask
        - requests
6. Pour pouvoir effectuer des requêtes sur l'API OMDb :
    - a. Générer votre clé API à travers l'URL suivante https://www.omdbapi.com/apikey.aspx en renseignant : **FREE! (1,0000 daily limit)**, votre **adresse mail**, **prénom**, **nom**, [**utilisation** : **Educational use for learning to use an API**]. Suivre les étapes pour activer votre clé.
    - b. Insérer votre clé dans *'api/api_secret.py'* avec ce nommage **key = '[votre clé générée]'**'
    - c. Pour que la requête fonctionne avec succès, un paramètre d'attribut de **movie** doit être renseigné, donc dans *'api/api_secret.py'* indiquez une valeur pour rechercher un film et commencer à créer un jeu d'essai. Nommage : **search_title = "&s=[movie title]"** (exemple : 'star' pour 'star wars', 'star trek')
7. Pour la connexion avec MiniNetflixDB avec l'app et pour alimenter votre jeu d'essai, les étapes sont les suivantes :
    - a. mettre à jour les valeurs dans *'db/db_secret.py'* avec ce nommage
        - **_un = "*[utilisateur configuré lors de l'installation d'Oracle DB]*"**
        - **_cs = "*[Hostname:Port configuré lors de l'installation d'Oracle DB]/[ServiceName configuré   lors  de l'installation d'Oracle DB]*"**
        - **_pw = '*[mot de passe choisi lors de l'installation d'Oracle DB]*'**
        - **_connection = None**

Vous êtes prêt à faire votre première requête pour fetcher des données de l'API donc
- 8. Démarrer l'app Flask
- 9. Créer un nouvel utilisateur puis se connecter avec celui-ci
- 10. Une fois la page d'accueil ouverte, mettez à jour l'URL en ajoutant l'endpoint */movies/callapi*
- 11. Un début de jeu d'essai sera alimenté dans la DB
- 12. Si vous voulez ajouter un autre film
    - a. Mettre à jour **search_title = "&s=[movie title]"** par une autre valeur souhaitée (exemple : 'harry potter')
    - b. Rédémarrer l'app Flask et répéter l'étape 10 ci-dessus


## Démarches de l'app livrée
1. Le script 'db/oracle.py' contient la méthode nécessaire pour la connexion avec la base de données Oracle
2. Les actions que l'on peut effectuer sur cette app ('login_process.py' et 'movie_processing.py') :
- s'inscrire en tant que nouvel utilisateur, se connecter et se déconnecter
- effectuer une requête sur une API pour récupérer des données d'un film et manipuler le format pour le spectre d'application du site en Flask.
- récupérer les données de l'ensemble des films présents dans la DB et l'afficher à l'utilisateur
- récupérer les données d'un film sélectionné présent dans la DB et afficher les détails à l'utilisateur
- rechercher un film par [titre, année de sortie, genre, acteur(s), langue, synopsis de l'intrigue]. Exemple : "devil" pour "The Devil Wears Prada"

## Répartition des tâches
| Navid SABETE ISFAHANI  | Tahina HONI RIKA |
| -------------          | ----------- |
| Initialisation du repo GitHub  + rédaction README        | Rédaction README 
| Création du script de création de la table **Movies** en fonction du modèle JSON de l'API        | Configuration de la connection Python<->Oracle + Création du script de la création de la table **Users** |
| Récupérer données - requêtes API + DB         | Récupérer données - requêtes API + DB   |
| Création jeu d'essai         | Création jeu d'essai   |
|  Movie processing (insert, getdatafromDB for dashboard, details, search)   | Login/Signup processing
|  Création templates Flask pour **Movies**   |  Création et optimisation templates Flask pour **Login** (optimisation pour **Login** et **Movies**) |
|  Optimisation finale de code     |    |
| Revue de code et tester app | Revue de code et tester app   | 

## Perspectives futures
- optimisation fonctionnelle (étendre le spectre d'application à d'autres types comme les séries - pour l'instant le jeu d'essai doit se limiter à des films pour assurer le modèle actuel opérationnel)
- optimisation de code (exemple : commentaire à ajouter pour la méthode *rows_to_dicts(cursor*) pour indiquer que l'on transforme les lignes data en un dictionnaire complet pour pouvoir mapper les variables sur les vues, opérations, etc.)