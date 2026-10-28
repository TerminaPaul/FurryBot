import requests
def mot_aleatoire() -> str:
    return requests.get('https://random-word-api.herokuapp.com/word?lang=fr').json()[0]


def recupere_description(mot):
    r = requests.get("https://fr.wiktionary.org/w/api.php",
        headers={"User-Agent": "Mot_Mystere"},
        params={"action": "query",
                "format": "json",
                "titles": mot.lower(),
                "prop": "extracts",
                "explaintext": "true",
                "redirects": "1",
        },
    )

    page = next(iter(r.json()["query"]["pages"].values())).get("extract")
    if "missing" in page:
        return None
    elif not est_francais(page):
        return None
    decouper = page.split("\n")

    paragraphes = []

    for n, ligne in enumerate(decouper):
        if not ligne: #Si ligne vide : retirer ligne
            decouper.remove(ligne)
        elif " == " in ligne and not est_francais(ligne):
            break
        elif ligne_est_balise(ligne):
            paragraphes.append([ligne,n,paragraphe(decouper,n)])

    return dictionnaire(mot,decouper, paragraphes)

def ligne_est_balise(ligne: str) -> bool:
    if "==" in ligne:
        return True
    return False


def paragraphe(decouper: list,n_ligne: int)-> tuple:
    taille_paragraphe = 1
    while True:

        if (n_ligne+taille_paragraphe) == len(decouper) or ligne_est_balise(decouper[n_ligne+taille_paragraphe]):
            return n_ligne+taille_paragraphe
        taille_paragraphe +=1


def est_francais(text: str)-> bool:
    if "== Français ==" in text:
        return True
    return False


def dictionnaire(mot,decouper, paragraphes):
    dico = {"mot":mot,"definition":[]}
    for paragraphe in paragraphes:
        text=""
        for ligne in range(paragraphe[1],paragraphe[2]-1):
            text+=decouper[ligne]
        #print(paragraphe[0],"\n",text,"\n")
        dico["definition"].append({"categories":paragraphe[0],"paragraphe":text})
    print(dico)
    """for i in dico["definition"]:
        print(i)"""
    #return dico

if __name__ == '__main__':
    #test = mot_aleatoire()
    #print(test)
    recupere_description("lancer")
