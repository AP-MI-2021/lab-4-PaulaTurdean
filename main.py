# TURDEAN PAULA-FLORINA - LABORATOR 4 - PARTIAL
def citire_lista():
    """
    Formeaza lista necesara prin citirea numarului de elemente si a elementelor propiu-zise.
    :return: Returneaza lista citita.
    """
    lst = []
    n = int(input("Dati nr. de elemente: "))
    print("Dati siruri de caractere formate din litere mici a-z, fara numere, simboluri sau spatii")
    for i in range(n):
        lst.append((input("l[" + str(i) + "]=")))
    return lst


def apare_in_lista(lista, sir):
    copie = lista[:]
    if copie.count(sir) > 0:
        return "DA"
    else:
        return "NU"


def test_apare_in_lista():
    assert apare_in_lista(['a', 'abc', 'def', 'b', 'ghi'], 'c') == "NU"
    assert apare_in_lista(['aaa', 'bbb', 'cmtc', 'drd', 'aaa'], 'drd') == "DA"
    assert apare_in_lista([], 'a') == "NU"


def elemente_care_se_repeta(lista):
    copie = lista[:]
    rezultat = []
    for x in copie:
        if copie.count(x) > 1:
            pass


def main():
    test_apare_in_lista()
    lista = []
    while True:
        print("1. Citire lista")
        print("2. Verificati dacă un șir de caractere citit de la tastatură se găsește în listă.")
        print("3. ")
        print("4. ")
        print("5. ")
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = citire_lista()


main()
