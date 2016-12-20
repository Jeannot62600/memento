__author__ = 'meliodas'


def createdata(chemin):
    datatxt = open(chemin, "r")
    fiche = datatxt.read()
    lignier = "".join(fiche).split("\n") #separe le fichier ligne par ligne dans un tableau
    objet = []
    y = 0
    for x in range(len(lignier)):
        ligne = lignier[x]
        z = 1
        if ligne.startswith(':#end'):
            break
        if ligne.startswith(":"):
            objet.append([])
            objet[y].append(ligne[1:].split("->")[0])
            objet[y].append(ligne[1:].split("->")[1].split(":")[1])
            objet[y].append(ligne[1:].split("->")[1].split(":")[0].split(","))
            objet[y].append(" ")
            ligne2 = lignier[x+z]
            while not(ligne2.startswith(":")):
                objet[y][3] += ligne2
                z += 1
                ligne2 = lignier[x+z]
            y += 1
    datatxt.close()
    return objet


def same(arg1,arg2):
    if arg1 == arg2 or arg2 == 0:
        return 1
    else: return 0


def datasearch(donnee,objet,type = 0):
    """
    :param donnee: l'expression recherche
    :param objet: dictionnaire des donnees
    :param type: type de l'objet recherche 0:default all,1:file,2:command
    :return: table of result in order of importance
    """
    donnees = []
    for don in objet:
        if same(don[1], type):
            if donnee in don[0]:
                donnees.append(don)
                objet.remove(don)
    for don in objet:
        if same(don[1], type):
            if donnee in "".join(don[2]):
                donnees.append(don)
    return donnees
