from random import random, randint, choice
carton = {
    "combien_de_ligne" : 2,
    "1" : [1, 2, 3, 4, 5],
    "2" : [45, 56, 23, 89, 67]
}

def afficher_carton(carton: dict) -> None:
    """Affiche le carton"""
    print("Votre carton :")
    for i in range(carton["combien_de_ligne"]):
        print(f"Ligne {i+1} : {carton[str(i+1)]}")

gagner = False

while not gagner:
    afficher_carton(carton)
    print("La roue tourne et à choisi un nombre")
    input("Appuyer pour continuer")

    print(f"Le nombre choisi : {...}")
    input("Appuyer pour continuer")