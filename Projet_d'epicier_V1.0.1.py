print("Le programme est en cours de développement!")
print("BONJOUR")
S = 0
while True:
    try:
        P = float(input(" ecrire le prix(Tapez 0 si vous souhaitez terminer): "))
        if P > 0:
            S = S + P
            print(str(S) + " DH")
            continue
        if P == 0:
            print("Montant total est " + str(S) + " DH")
            break
        else:
            print("ERROR! La valeur que vous avez saisie est inférieure à 0.")
            continue
    except:
        print("les caractères ne sont pas des valeure de calcule")
        continue

# les erreurs et points faibles identifiés dans la version V1.0.0 :
# Gestion des exceptions trop générale : L’utilisation de except: sans préciser le type d’erreur attrape tout, y compris les interruptions clavier, ce qui peut cacher de vrais bugs et rendre le débogage difficile.
# Validation de saisie négative : Si un nombre négatif est saisi, l’utilisateur reçoit un message d’erreur, mais le programme propose seulement de ressaisir sans expliquer comment corriger.
# Message d’erreur pour caractères non numériques : Le message ("les caractères ne sont pas des valeure de calcule") s’affiche pour toute erreur de saisie non numérique, ce qui manque de précision (erreur de frappe, espace vide, etc.).
# Positionnement du total : Risque d’affichage incorrect du montant total si l’indentation est mal gérée en dehors de la boucle.
# Exception non ciblée : Le bloc try/except englobe toute la saisie et son traitement, ce qui empêche de repérer où l’erreur se produit exactement (entrée, addition, affichage).
# Utilisation de float sans validation : Les entrées telles que “5,50” peuvent causer une erreur selon la locale du clavier (virgule au lieu de point).