import requests
#https://fr.wiktionary.org/w/api.php?action=query&format=json&origin=*&prop=extracts&explaintext=true&redirects=1&titles=maison

#https://random-word-api.herokuapp.com/word?lang=fr

def mot_aleatoire():
    return requests.get('https://random-word-api.herokuapp.com/word?lang=fr').json()[0]


def mot_existe(mot):
    r = requests.get(
        "https://fr.wiktionary.org/w/api.php",
        headers={"User-Agent": "Mot_Mystere"},
        params={"action": "query", "format": "json", "titles": mot},
    )
    page = next(iter(r.json()["query"]["pages"].values()))
    return "missing" not in page



if __name__ == '__main__':
    test = mot_aleatoire()
    print(test)
    print(mot_existe(mot_aleatoire()))