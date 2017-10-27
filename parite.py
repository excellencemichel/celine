#! /usr/bin/env python3  
# coding: utf-8


"""
  Quand un fichier avec l'interpreteur python ce dernier défini
  plusieur variables spéciales avant la lecture du fichier

  Par exemple :
    Pour lire un fichier l'interpreteur defini la 
    variable __name__
    Si le fichier est exécuter en tant que programe
    principal cette variable vaut __main__
    Si le fichier est importer en tant que module
    cette variable vaut le nom du module 
"""


def main():
	pass


if __name__ == '__main__':
	main()