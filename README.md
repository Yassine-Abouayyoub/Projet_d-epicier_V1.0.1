# Projet_d-epicier_V1.0.1
Projet_d'epicier_V1.0.1, Cette version apporte des corrections de bugs et améliore la robustesse du programme.

## 1. Fonctionnalités:
- Saisie des prix sous forme de nombres réels (float).

- Affichage du sous-total après chaque saisie.

- Instructions claires pour terminer la saisie (taper 0).

- Gestion des entrées non numériques : affiche un message d’erreur et invite à ressaisir.

- Message dédié pour valeurs négatives.

- Affichage du montant total en fin de saisie.

## 2. Bugs corrigés / Erreurs techniques:
- Empêche le plantage en cas de saisie non numérique.

- Affiche l’erreur correspondante selon le type de saisie.

- Sépare l’affichage du sous-total et du total final avec une meilleure indentation.

- Sécurise la saisie en utilisant une gestion d’exception.

## 3. Points à améliorer:
- La gestion des exceptions reste trop générale (except: global).

- Les messages d’erreur pourraient être rendus encore plus précis selon le contexte.

- Les cas particuliers (virgule, espace, etc.) ne sont pas entièrement gérés.
