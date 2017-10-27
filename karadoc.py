if __name__ =="__main__":
	""" Ici nous testons s fichier est exécuter en tant que programme principale
	    ce qui est dans le bloc if va s'exécuter
	    Mais si le fichier est importé à ailleurs dans d'autres fichiers comme 
	    module c'est ce qui est dans else qui va s'exécuter
	    """
	print("""Les chicots, c'est sacré!
		parce que j'les lave pas maintentant,
		 dans dix ans, c'esst tout à la soupe.
		 Et l'mec qui ne fera me fera manger de 
		 soupe il est pas né !""")

else:
	"""
	   Si le fichier est importé ailleurs c'est ici qui va s'exécuter
	"""
	print("Du passé faisons table en marbre. ")