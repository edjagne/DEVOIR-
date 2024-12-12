import random
# Liste des régions et leurs chefs-lieux
regions = {
    "Agnéby-Tiassa": "Agboville",
     "Bafing": "Touba",
    "San Pedro": "San Pedro",

    "Gontougo": "Bondoukou",
    "Bagoué": "Boundiali",
    "Marahoué": "Bouaflé",
    "Haut-Sassandra": "Daloa",
   "Worodougou": "Suéguéla",
    "Bélier": "Toumodi",
     "Béré": "Mankono",
    "Bounkani": "Bouna",
    "Cavally": "Guiglo",
    "Folon": "Minignan",
   "Gbôklé": "Sassandra",
}
# Simulation d'une base de données des scores
scores = []
def afficher_meilleurs_scores():
    """Affiche les 5 meilleurs scores."""
    print("\n--- Meilleurs Scores ---")
    meilleurs_scores = sorted(scores, reverse=True)[:5]
    for i, score in enumerate(meilleurs_scores, start=1):
        print(f"{i}. {score} points")
    print()
def poser_question(region, chef_lieu):
    """Pose une question et retourne si la réponse est correcte ou non."""
    print(f"Quel est le chef-lieu de la région {region} ?")
    reponse = input("Votre réponse : ").strip()
    if reponse.lower() == chef_lieu.lower():
        print("Bonne réponse !")
        return True
    else:
        print(f"Mauvaise réponse. La bonne réponse est : {chef_lieu}.")
        return False
def jouer():
    """Démarre une partie de jeu."""
    print("\n--- Nouvelle Partie ---")
    afficher_meilleurs_scores()
    questions_posees = set()
    score = 0
    for _ in range(10):  # 10 questions par partie
        while True:
            region, chef_lieu = random.choice(list(regions.items()))
            if region not in questions_posees:
                questions_posees.add(region)
                break
        if poser_question(region, chef_lieu):
            score += 1
    print(f"\nVotre score final : {score} / 10")
    scores.append(score)
# Programme principal
while True:
    print("\n1. Jouer")
    print("2. Quitter")
    choix = input("Votre choix : ").strip()
    if choix == "1":
        jouer()
    elif choix == "2":
        print("Merci d'avoir joué !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")

