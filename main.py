# ----------------------------------------------------------------------------- #
#       Formation Administrateur Infrastructure et Cloud OpenClassRooms         #
#         Projet 6 : Participer à la vie de la communauté Open Source           #
#                              CECCHINATO Quentin                               #
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- #
#      Programme d'installation et de configuration de Windows Serveur 2019     #

# Rôle : Ce programme sera composé de 3 fonctions qui vont installer et         #
#        configurer, avec un paramétrage basique, un Windows serveur 2019.      #
# ----------------------------------------------------------------------------- #

import subprocess
import sys

#                                  Les Fonctions                                #


# ----------------------------------------------------------------------------- #
#                        Fonction 1 : ConfigurerIPNom()                         #

# Rôle : Avec cette fonction on va pouvoir configurer l'adresse IP, le masque   #
#        de sous-réseeu, le DNS, la passerelle par défaut et le nom du Windows  #
#        Serveur 2019.                                                          #

#                               ConfigurerIPNom()                               #

def configureripnom():
    print("Bienvenue dans la configuration IP et Nom du serveur Windows.")

    # appel du script powershell IPNom
    p = subprocess.Popen(["powershell.exe",
                          "C:\\powershell\\IPNom.ps1"],
                         stdout=sys.stdout)
    p.communicate()
    print("Vous avez terminé la configuration IP et Nom du serveur Windows.")
    pass


#                                      Fin                                      #
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#                        Fonction 2 : InstallationDHCP()                        #

# Rôle : Cette fonction va insaller le service DHCP sans le configurer          #

#                               InstallationDHCP()                              #

def installationdhcp():
    print("Bienvenue dans l'installation du service DHCP.")

    # appel du script powershell DHCP
    p = subprocess.Popen(["powershell.exe",
                          "C:\\powershell\\DHCP.ps1"],
                         stdout=sys.stdout)
    p.communicate()
    print("Vous avez terminé l'installation du service DHCP.")
    pass


#                                      Fin                                      #
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#                        Fonction 3 : InstallationAD()                          #

# Rôle : Cette fonction va insaller le service AD et le configurer (simplement) #

#                               InstallationAD()                                #

def installationad():
    print("Bienvenue dans l'installation du service AD.")

    # appel du script powershell AD
    p = subprocess.Popen(["powershell.exe",
                          "C:\\powershell\\AD.ps1"],
                         stdout=sys.stdout)
    p.communicate()
    print("Vous avez terminé l'installation du service AD.")
    pass


#                                      Fin                                      #
# ----------------------------------------------------------------------------- #


# ----------------------------------------------------------------------------- #
#      Programme d'installation et de configuration de Windows Serveur 2019     #

# Rôle : Ce programme sera composé de 3 fonctions qui vont installer et         #
#        configurer, avec un paramétrage basique, un Windows serveur2019.       #

#                   Programme : Installer&ConfigurerWinSV2019                   #

Oui = "o"
Non = "n"

reponse = input("Bonjour, voulez vouz configurer Windows Serveur 2019 ? (Oui : o Non : n) : ")
if reponse == Oui:
    print("Nous allons commencer l'installation.")

    print("Première étape : Configuration de l'adressage IP et du Nom du Serveur Windows")
    configureripnom()

    print("Deuxième étape : Installation du service DHCP")
    installationdhcp()

    print("troisième étape : Installation du service AD")
    installationad()

    print("Vous avez terminer la configuration de votre serveur Windows.")
    print("Le serveur va redemarrer.")

# Au début j'avais noté ça : elif reponse == Non :
else:
    print("La configuration a été annulé.")
pass

#                                      Fin                                      #
# ----------------------------------------------------------------------------- #



