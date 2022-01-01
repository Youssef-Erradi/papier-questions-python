# encoding:utf-8
from itertools import combinations_with_replacement

def calculer_notes_possibles(n,a,b):
    if 1<=n<=5*10**4 and 1<=a<=20 and -20<=b<=-1:
        notes_possibles = set()
        for combination in combinations_with_replacement([0,a,b], n):
            notes_possibles.add(sum(combination))
        print(len(notes_possibles)," =>", sorted(notes_possibles))
    else:
        print("** Erreur : les valeurs de N, a et b doivent être : 1⩽N⩽5x10⁴ et 1⩽a,b⩽20 **")

def main(nom_fichier="Fichier d'entrée.txt"):
    with open(file=nom_fichier, mode="r") as fichier :
        T = 0
        if fichier.tell() == 0 :
            T = fichier.readline().strip()
            if T.isdecimal() and (1<=int(T)<=50):
                T = int(T)
            else: 
                print("** Erreur : la valeur de T doit être un entier entre 1 et 50 **")
                exit(0)
        for _ in range(T):
            try:
                donnees = fichier.readline().strip().split(" ")
                if len(donnees) != 3 :
                    print("** Erreur : ligne vide ou format incorrecte **")
                    continue
                n, a, b = tuple(donnees)
                n, a, b = int(n), int(a), int(b)*-1
                calculer_notes_possibles(n,a,b)
            except ValueError:
                print("** Erreur : Vous douvez entrer trois valeurs entières **")
  
if __name__ == '__main__':
    main()
