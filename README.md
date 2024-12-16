# Projet LITReview
LITReview est un site permettant de publier des critiques de livres ou d’articles et de consulter ou de solliciter une critique de livres à la demande.
## Cloner le projet

````bash
$ https://github.com/Jogodev/LITReview.git
$ cd litreview
````

### Créer l'environnement virtuel

````bash
$ python -m venv env
````

### Activer l'environnement virtuel

#### Windows
````bash
$ . env\scripts\activate
````
#### Mac
````bash
$ source env\bin\activate
````
#### linux
````bash
$ source env\bin\activate
````

### Installer les paquets

````bash
$ pip install -r requirements.txt
````

### Se déplacer dans le second dossier litreview
````bash
$ cd litreview
````
### Lancer la commande
````bash
$ python manage.py runserver
````

### Sur votre navigateur rendez vous a l'adresse http://127.0.0.1:8000/

#### Inscrivez vous ou connectez vous avec un des utilisateurs suivant :
| **Utilisateur** | **Mot de passe** |
|-----------------|------------------|
| John            | Litreview123     |
| Bob             | Litreview123     |
| Alain           | Litreview123     |

### Fonctionnalités
#### Non connecté
* Inscription
* Connexion
#### Connecté
* Créer des ticket de demande de critique
* Créer des critiques
* Voir, Modifier, supprimer vos tickets et vos critiques
* Un flux avec vos tickets, critiques et ceux des utilisateurs que vous suivez
* S'abonner à des utilisateurs et se désabonner
