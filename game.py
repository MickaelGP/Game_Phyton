import random


def choix_ordi():
    c = ["pierre", "papier", "ciseaux"]
    choix_pc = random.choice(c)
    return choix_pc


def pierre_papier_ciseau():
    print("=== Bienvenue dans le jeu pierre papier ciseaux ===")
    print("Voici les différents choix possibles :")
    print("Pierre")
    print("Papier")
    print("Ciseaux")
    print("0. Sortir")

    score_joueur = 0
    score_ordi = 0

    while True:
        print("Scores - Joueur:", score_joueur, " Ordi:", score_ordi)

        choix = input("Faites un choix entre pierre, papier, ciseaux ou 0 pour sortir :")
        ordi = choix_ordi()

        if choix == '0':
            print("Au revoir")
            break
        elif choix == 'pierre' and ordi == 'ciseaux':
            print("Vous gagnez cette manche")
            score_joueur += 1
        elif choix == 'papier' and ordi == 'pierre':
            print("Vous gagnez cette manche")
            score_joueur += 1
        elif choix == 'ciseaux' and ordi == 'papier':
            print("Vous gagnez cette manche")
            score_joueur += 1
        elif choix == ordi:
            print("Match nul")
        else:
            print("L'ordi gagne cette manche")
            score_ordi += 1

        if score_joueur == 5 or score_ordi == 5:
            print("Partie terminée!")
            if score_joueur == 5:
                print("Vous avez gagné la partie!")
            else:
                print("L'ordinateur a gagné la partie!")
            relancer = input("Voulez-vous relancer le jeu ? (Oui/Non) : ")
            if relancer.lower() == "oui":
                score_joueur = 0
                score_ordi = 0
            else:
                print("Au revoir!")
                break


pierre_papier_ciseau()
