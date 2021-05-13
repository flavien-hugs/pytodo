# menu a afficher
__author__ = 'Flavien-hugs <flavienhugs@pm.me>'
__copyright__ = '© 2015 unsta'

from src import todo

def menu():
    print("1 - Ajouter un élève.")
    print("2 - Rechercher un élève.")
    print("3 - Voir la liste des élèves.")
    print("4 - Quiter.")

    choice = str(input("\n - Choisissez une option : "))

    if choice == "1":
        # appelle de la fonction
        todo.add_student()
        menu()
    elif choice == "2":
        # appelle de la fonction
        todo.search_student()
        menu()
    elif choice == "3":
        # appelle de la fonction
        todo.read_student_list()
        menu()
    elif choice == "4":
        print("Fin du programme.")
    else:
        print("Option invalide ! \n")
        menu()

if __name__ == '__main__':
    menu()
