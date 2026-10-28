MotDuJour = "FURRY"


def main(mot) -> bool | str:
    mot = maj(mot)
    for lettre in mot:
        if not lettre_in_alphabet(lettre):
            return False
    if not len_mot_is_correct(mot):
        return False
    answer = verification(mot)
    return answer


def maj(mot: str) -> str:
    return mot.upper()


def lettre_in_alphabet(lettre: str) -> bool:
    if not lettre.isalpha():
        return False
    return True


def len_mot_is_correct(mot: str) -> bool:
    if len(mot) != len(MotDuJour):
        return False
    return True


def verification(proposition: str) -> str:
    liste_lettre = {}

    for l in MotDuJour:
        liste_lettre[l] = 1 if l not in liste_lettre else liste_lettre[
                                                              l] + 1  # rajoute les lettres de MotDuJour dans un Dictionnaire

    answer = [""] * len(MotDuJour)

    for i, lettre in enumerate(proposition):
        if lettre == MotDuJour[i]:
            answer[i] = "✅"
            liste_lettre[lettre] -= 1

    for j, lettre in enumerate(proposition):
        if answer[j] == "":
            if lettre in MotDuJour and liste_lettre[lettre] > 0:
                answer[j] = "🟨"
                liste_lettre[lettre] -= 1
            else:
                answer[j] = "🟥"

    answer = "".join(answer)
    return answer


def mot_completer(mot: str) -> bool:
    for caractere in mot:
        if caractere != "✅":
            return False
    return True


if __name__ == '__main__':
    MotDuJour = "aventurismes".upper()
    print(f"Il faut trouver un mot de : {len(MotDuJour)} lettres")
    while True:
        ans = main(input())
        print(ans)
        if mot_completer(ans):
            print("GG tu as trouvé le mot du jour")
            break
