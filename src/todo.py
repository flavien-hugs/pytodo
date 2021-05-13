__author__ = 'Flavien-hugs <flavienhugs@pm.me>'
__copyright__ = '© 2015 unsta'


# fonction permettant d'enregistrer les élèves
def add_student():
    # ouverture du fichier
    file = open("data/student_list.txt", "a")

    # ajouter un élève
    student_first_name = str(input("Entrer le nom de l'élève: "))
    student_last_name = str(input("Entrer le prénom de l'élève: "))
    # ecriture dans le fichier
    file.write("{0} {1}".format(student_first_name.upper(), student_last_name.capitalize()))
    # fermeture du fichier
    file.close()

    # message d'enregistrement
    print(
        "Vous avez ajouté l'élève: \n\
        Nom : {0} \n Prénom: {1}\n\
        Élève ajouté avec succès.".format(
            student_first_name, student_last_name
        )
    )


# lire le contenu du fichier ligne par ligne
def read_student_list():
    file = open("data/student_list.txt", "r")
    print("Liste des étudiants: \n")
    for n in file:
        print(n)
    file.close()


# rechercher un élève
def search_student():
    file = open("data/student_list.txt", "r")
    search = str(input("Entrer le nom ou prénom de l'élève : \n"))
    if search in file.read():
        print("{0} existe dans la liste des élèves. \n\n".format(search))
    else:
        print("{0} n'existe pas dans la liste des élèves. \n\n".format(search))
    file.close()
